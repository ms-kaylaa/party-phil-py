import discord

import os

from globals import USER_DIR

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    user_dir = f"{USER_DIR}{message.author.id}/files"

    filename = " ".join(args)
    path = user_dir + "/" + filename

    if os.path.exists(path):
        os.remove(path)
        await message.channel.send("deleted " + filename)
    else:
        await message.channel.send("you have not uploaded a file with that name")