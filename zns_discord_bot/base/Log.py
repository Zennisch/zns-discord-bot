import logging
from typing import Optional

from discord.utils import MISSING
from zns_logging import ZnsLogger


class Log(ZnsLogger):
    def __init__(
        self,
        reconnect: bool = True,
        log_handler: Optional[logging.Handler] = MISSING,
        log_formatter: logging.Formatter = MISSING,
        log_level: int = MISSING,
        root_logger: bool = False,
    ):
        super().__init__(__name__, log_level)

        self.reconnect = reconnect
        self.log_handler = log_handler
        self.log_formatter = log_formatter
        self.log_level = log_level
        self.root_logger = root_logger

        self.__init()

    def __init(self):
        if not self.log_handler:
            self.log_handler = ZnsLogger(__name__, self.log_level).handlers[0]

        if not self.log_formatter:
            self.log_formatter = self.log_handler.formatter
