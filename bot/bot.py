# bot.py
import discord
from bot import aws_resources as aws
from discord.ext import commands

# Connecting to Discord
discord_client = discord.Client()

rhelbot = commands.Bot(command_prefix='!rhel ')


# Bot startup information
@rhelbot.event
async def on_ready(self):
    print(f'Connected to Discord!\n\n')
    print(f'{rhelbot.user} is connected to the following Discord servers:\n')
    for guild in rhelbot.guilds:
        print(f'{guild.name} (id: {guild.id})\n')


# Per-server welcome messages
@rhelbot.event
async def on_member_join(member):
    welcome_message = aws.fetch_server_welcome(member.guild.id)
    if welcome_message == 'Error':
        return
    else:
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to {member.guild.name}!\n\n'
            f'{welcome_message}'
        )
        return


# Starting the bot up
aws.fetch_bot_token()
bot_token_file = open("rhelbot_token.txt", "r")
bot_token = bot_token_file.read()
rhelbot.run(bot_token)