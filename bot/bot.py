# bot.py
# Generic version of the bot for other servers
import discord
from discord.ext import commands
from aws_resources import fetch_server_welcome, fetch_bot_token

# Connecting to Discord
discord_client = discord.Client()

# Setting up the Cog imports
# Prod cogs
initial_extensions = ['cogs.admin']


# Setting the command handler
rhelbot = commands.Bot(command_prefix='!rhel ')

# Loading the Cogs into the bot
for extension in initial_extensions:
    try:
        rhelbot.load_extension(extension)
        print(f'Successfully loaded Cog {extension}')
    except commands.ExtensionError as e:
        print(f'Failed to load Cog {extension} with error {e}')


# Bot startup information
@rhelbot.event
async def on_ready():
    print(f'Rhelbot has connected to Discord!\n\n')
    print(f'{rhelbot.user} is connected to the following Discord servers:\n')
    for guild in rhelbot.guilds:
        print(f'{guild.name} (id: {guild.id})\n')


# Per-server welcome messages
@rhelbot.event
async def on_member_join(member):
    welcome_message = fetch_server_welcome(member.guild.id)
    if welcome_message == ('Error' or ''):
        return
    else:
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to the {member.guild.name} Discord server!\n\n'
            f'{welcome_message}'
        )
        return


# Starting the bot up
fetch_bot_token()
bot_token_file = open("rhelbot_token.txt", "r")
bot_token = bot_token_file.read()
rhelbot.run(bot_token, bot=True, reconnect=True)
