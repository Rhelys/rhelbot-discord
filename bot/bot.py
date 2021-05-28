# bot.py
# Generic version of the bot for other servers
import logging
import discord
from discord.ext import commands
from bot_functions.aws_resources import fetch_server_welcome, fetch_bot_token, fetch_server_reactions
# from bot_functions.reactions import reaction_add, reaction_remove

# Setting up logs
rhelbot_logs = logging.getLogger('discord')
rhelbot_logs.setLevel(logging.WARN)
handler = logging.FileHandler(filename='rhelbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
rhelbot_logs.addHandler(handler)

# Connecting to Discord
discord_client = discord.Client()

# Setting up the Cog imports - Prod only in this list
initial_extensions = ['cogs.admin', 'cogs.fflogs']


# Setting multiple help prefixes
def get_help_prefix(bot, message):
    prefixes = ['help', '?', 'wut']

    # Only allow for 'help' in DMs
    if not message.guild:
        return 'help'
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Also setting custom ways to interact with the bot
def get_command_prefix(bot, message):
    prefixes = ['!rhel ']

    # Only allow for the default in DMs
    if not message.guild:
        return '!rhel '

    # Allow the bot to also respond to mentions as if it's a prefix
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Setting the command handler
rhelbot = commands.Bot(command_prefix=get_command_prefix, default_help_command=get_help_prefix,
                       description='Rhelbot - the bot for Rhelys to do stuff')

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
