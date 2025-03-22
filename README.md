<h1 align="center">zns-discord-bot</h1>

<h3 align="center">A Discord bot library that integrates many functionalities for Python</h3>

# Installation
```bash
pip install zns-discord-bot
```

# Usage
```python
from discord import Intents

from zns_discord_bot.ZnsDiscordBot import ZnsDiscordBot

bot = ZnsDiscordBot(
    token="YOUR.DISCORD.BOT.TOKEN",
    command_prefix="!",
    intents=Intents.default(),
)

if __name__ == "__main__":
    bot.init()
```

# Features
(Will be updated soon)

# Change Log
```markdown
1.0.0

- Status: Yanked
- Change: Initial release
- Reason: Wrong README.md documentation

1.0.1

- Status: Yanked
- Change: Fix README.md documentation
- Reason: `log_level` default value in `Logging` class is not set

1.0.2

- Status: Released
- Change: Fix `log_level` default value in `Logging` class
```
