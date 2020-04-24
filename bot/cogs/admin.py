# admin.py
# This file holds the commands cog for all privileged commands

import discord
from discord.ext import commands


class AdminCog(commands.Cog, name="Admin Commands"):
    def __init__(self, rhelbot):
        self.bot = rhelbot
        self._last_member = None

    @commands.command(name='create-channel', help='Creates a text channel with the specified name')
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, channel_name):
        server = ctx.guild
        existing_channel = discord.utils.get(server.channels, name=channel_name)
        if not existing_channel:
            await ctx.send(f'Text channel #{channel_name} created!')
            await server.create_text_channel(channel_name)


def setup(rhelbot):
    rhelbot.add_cog(AdminCog(rhelbot))
