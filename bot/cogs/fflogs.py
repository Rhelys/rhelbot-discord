# fflogs.py
# This file contains the logic for the fflogs lookup command

import requests
import json
import discord
from discord.ext import commands
from bot_functions.graphQL_queries import allstar


class FflogsCog(commands.Cog, name="FFLogs Commands"):
    def __init__(self, rhelbot):
        self.bot = rhelbot
        self._last_member = None

    @commands.command(name='fflogs', help='Looks up a character name and server combo')
    async def fflogs(self, ctx, first_name, last_name, ff_server):
        discord_server = ctx.guild
        character_name = first_name + " " + last_name
        await ctx.send(f'Understood character name "{character_name}" on server "{ff_server}"')


def setup(rhelbot):
    rhelbot.add_cog(FflogsCog(rhelbot))
