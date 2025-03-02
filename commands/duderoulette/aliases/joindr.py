import discord

from commands.duderoulette import joinduderoulette

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    joinduderoulette.run(message, args, client)