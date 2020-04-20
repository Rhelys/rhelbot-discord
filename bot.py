# bot.py
import discord
import aws_resources as aws

# Connecting to Discord
discordClient = discord.Client()


@discordClient.event
async def on_ready():
    print(f'Connected to Discord!\n\n')
    print(f'{discordClient.user} is connected to the following Discord servers:\n')
    for guild in discordClient.guilds:
        print(f'{guild.name} (id: {guild.id})\n')


aws.fetchBotToken()
botTokenFile = open("rhelbot_token.txt", "r")
botToken = botTokenFile.read()
discordClient.run(botToken)