import discord

from commands.duderoulette import newduderoulette

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    newduderoulette.run(message, args, client)