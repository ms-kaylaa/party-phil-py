import discord

from commands.duderoulette import leaveduderoulette

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    leaveduderoulette.run(message, args, client)