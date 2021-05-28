# reactions.py
# This file holds the functions for all server-specific actions based on message reactions

import discord
from discord.ext import commands
from bot.bot_functions.aws_resources import fetch_server_reactions


def reaction_add(reaction, member):
    reaction_data = fetch_server_reactions(member.guild.id)
    if not reaction_data:
        return
    else:
        if reaction.message.id == reaction_data['reaction_message_id']:
            for emote in reaction_data['emote_name']:
                if emote == reaction.emote.name:
                    return

        else:
            return


def reaction_remove(reaction, member):
    reaction_data = fetch_server_reactions(member.guild.id)
    if not reaction_data:
        return
    else:
        return
