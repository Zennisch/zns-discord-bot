import logging
from typing import Optional

from zns_logging import ZnsLogger


class LogBase:
    def __init__(
        self,
        reconnect: bool = True,
        log_handler: Optional[logging.Handler] = None,
        log_formatter: logging.Formatter = None,
        log_level: int = logging.INFO,
        root_logger: bool = False,
    ):
        self.reconnect = reconnect
        self.log_handler = log_handler
        self.log_formatter = log_formatter
        self.log_level = log_level
        self.root_logger = root_logger

        self._process_log_base()

    def _process_log_base(self):
        if not self.log_handler:
            logger = ZnsLogger(__name__, self.log_level)
            for handler in logger.handlers:
                if isinstance(handler, logging.StreamHandler):
                    self.log_handler = handler
                    break

        if not self.log_formatter:
            self.log_formatter = self.log_handler.formatter
