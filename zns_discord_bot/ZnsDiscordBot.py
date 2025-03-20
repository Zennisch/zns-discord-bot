import asyncio
import logging
from typing import Type, Iterable, Optional

from discord import Intents, utils
from discord.ext.commands import Bot
from discord.utils import MISSING

from zns_discord_bot.base.Log import Log


class ZnsDiscordBot(Bot, Log):
    def __init__(
        self,
        token: str,
        command_prefix: Type[Iterable[str] | str | tuple],
        intents: Intents,
        **options,
    ):
        super().__init__(command_prefix, intents=intents, **options)
        Log.__init__(self, **options)

        self.__token = token

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

        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            return

    def init(self):
        self.run(
            self.__token,
            reconnect=self.reconnect,
            log_handler=self.log_handler,
            log_formatter=self.log_formatter,
            log_level=self.log_level,
            root_logger=self.root_logger,
        )
