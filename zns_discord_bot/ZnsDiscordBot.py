from typing import Type, Iterable

from discord import Intents
from discord.ext.commands import Bot

from zns_discord_bot.base.LogBase import LogBase


class ZnsDiscordBot(Bot, LogBase):
    def __init__(
        self,
        token: str,
        command_prefix: Type[Iterable[str] | str | tuple],
        intents: Intents,
        **options,
    ):
        super().__init__(command_prefix, intents=intents, **options)
        LogBase.__init__(self, **options)

        self.__token = token

    def init(self):
        self.run(
            self.__token,
            reconnect=self.reconnect,
            log_handler=self.log_handler,
            log_formatter=self.log_formatter,
            log_level=self.log_level,
            root_logger=self.root_logger,
        )
