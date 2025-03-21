<h1 align="center">zns-discord-bot</h1>

<h3 align="center">A Discord bot library that integrates many functionalities for Python</h3>

# Installation
```bash
npm install zns-discord-bot
```

# Usage
```python
from discord import Intents

from zns_discord_bot.ZnsDiscordBot import ZnsDiscordBot

bot = ZnsDiscordBot(
    token="YOUR.DISCORD.BOT.TOKEN",
    command_prefix="!",
    intents=Intents.default()
)

if __name__ == "__main__":
    bot.init()
```

# Features
(Will be updated soon)

# Change Log
```markdown
1.0.0
- Status: Released
- Changes: Initial release
```
