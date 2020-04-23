# goe.py
# Server-specific config for the Garden of Eden (Server ID:390949449372794882)

import bot as bot
import discord
from discord.ext import commands

rhelbot = commands.Bot(command_prefix='!rhel ')


# Validating that we've connected to the right server. Looking for the Garden of Eden
@rhelbot.event
async def on_ready():
    print(f'Connected to Discord!\n\n')
    print(f'{rhelbot.user} is connected to the following Discord servers:\n')
    for guild in rhelbot.guilds:
        if guild.id == 390949449372794882:
            print(f'Rhelbot has successfully connected to {guild.name}')
        else:
            return
