# admin.py
# This file holds the commands cog for all privileged commands

import discord
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, rhelbot):
        self.bot = rhelbot
        self._last_member = None

    @commands.command(name='create-channel')
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, channel_name):
        server = ctx.guild
        existing_channel = discord.utils.get(server.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel in {server.name} called {channel_name}')
            await server.create_text_channel(channel_name)


def setup(rhelbot):
    rhelbot.add_cog(AdminCog(rhelbot))
