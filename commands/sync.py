import discord

from sync import sync

# EAT SHIT HEXOSE
async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    await sync(message)