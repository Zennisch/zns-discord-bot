import asyncio
import logging
import traceback
from typing import Type, Iterable, Optional

from discord import Intents, utils
from discord.ext.commands import Bot
from discord.utils import MISSING
from zns_logging import ZnsLogger

from zns_discord_bot.base.Logging import Logging


class ZnsDiscordBot(Bot, Logging):
    """
    A Discord bot class that integrates logging functionalities.

    Args:
        token (str): The bot's authentication token.
        command_prefix (Iterable[str] | str | tuple): The command prefix for the bot.
        intents (Intents): The Discord intents required for bot operation.
        **options: Additional configuration options for both the bot and logging.
    """

    def __init__(
        self,
        token: str,
        command_prefix: Type[Iterable[str] | str | tuple],
        intents: Intents,
        *,
        log_file_path_sys: str = None,
        log_file_path_bot: str = None,
        **options,
    ):
        Bot.__init__(self, command_prefix=command_prefix, intents=intents, **options)
        Logging.__init__(self, file_path=log_file_path_bot, **options)

        self._token = token
        self._log_file_path_sys = log_file_path_sys

    def run(
        self,
        token: str,
        *,
        reconnect: bool = True,
        log_handler: Optional[logging.Handler] = MISSING,
        log_formatter: logging.Formatter = MISSING,
        log_level: int = MISSING,
        root_logger: bool = False,
    ) -> None:
        async def runner():
            async with self:
                await self.start(token, reconnect=reconnect)

        async def wait_for_user():
            while not self.user:
                await asyncio.sleep(1)
            self.name = self.user.name

        async def main():
            await asyncio.gather(runner(), wait_for_user())

        if log_handler is not None:
            utils.setup_logging(
                handler=log_handler,
                formatter=log_formatter,
                level=log_level,
                root=root_logger,
            )
            if self._log_file_path_sys:
                log_handler = ZnsLogger(__name__, self.log_level, file_path=self._log_file_path_sys).handlers[1]
                if root_logger:
                    logger = logging.getLogger()
                    logger.addHandler(log_handler)
                else:
                    library, _, _ = utils.__name__.partition(".")
                    logger = logging.getLogger(library)
                    logger.addHandler(log_handler)

        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            self.info(f"Bot stopped by user")
        except Exception as e:
            self.error(f"Bot stopped with error: {e}")
            self.error(traceback.format_exc())

    def init(self):
        self.run(
            self._token,
            reconnect=self.reconnect,
            log_handler=self.log_handler,
            log_formatter=self.log_formatter,
            log_level=self.log_level,
            root_logger=self.root_logger,
        )
