import discord
import sys

import stat_handler

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    stat_handler.save_stats()
    await message.channel.send("Self destructing")
    sys.exit(0)
    pass