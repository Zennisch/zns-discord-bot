import logging
from typing import Type, Iterable, Optional

from discord import Intents
from discord.ext.commands import Bot
from zns_logging import ZnsLogger


class ZnsDiscordBot(Bot):
    def __init__(
            self,
            token: str,
            command_prefix: Type[Iterable[str] | str | tuple],
            intents: Intents,
            *,
            reconnect: bool = True,
            log_handler: Optional[logging.Handler] = None,
            log_formatter: logging.Formatter = None,
            log_level: int = logging.INFO,
            root_logger: bool = False,
            **options,
    ):
        super().__init__(command_prefix, intents=intents, **options)

        self.__token = token
        self.reconnect = reconnect
        self.log_handler = log_handler
        self.log_formatter = log_formatter
        self.log_level = log_level
        self.root_logger = root_logger

    def init(self):
        if not self.log_handler:
            logger = ZnsLogger(__name__, self.log_level)
            for handler in logger.handlers:
                if isinstance(handler, logging.StreamHandler):
                    self.log_handler = handler
                    break

        if not self.log_formatter:
            self.log_formatter = self.log_handler.formatter

        self.run(
            self.__token,
            reconnect=self.reconnect,
            log_handler=self.log_handler,
            log_formatter=self.log_formatter,
            log_level=self.log_level,
            root_logger=self.root_logger,
        )
