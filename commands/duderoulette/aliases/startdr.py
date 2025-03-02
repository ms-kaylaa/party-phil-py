import discord

from commands.duderoulette import startduderoulette

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    startduderoulette.run(message, args, client)