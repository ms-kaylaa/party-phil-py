import discord

import stat_handler

import os
import threading

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    def run():
        os.system("python main.py")

    stat_handler.save_stats()
    threading.Thread(target=run).start()
    await message.channel.send("Killing this instance")
    client.close()
    exit()