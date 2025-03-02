import discord

import os
import random

from globals import FILE_DIR

file_list = []
def recursive_get_all_files(dir):
    for file in os.listdir(dir):
        #await msg.channel.send(file)
        if os.path.isdir(dir + file + "/"):
            #await msg.channel.send("entered this dir ^")
            recursive_get_all_files(dir + file + "/")
            #await msg.channel.send("exited dir " + dir)
        else:
            file_list.append(dir + file)

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    recursive_get_all_files(FILE_DIR)
    
    await message.reply(file=discord.File(random.choice(file_list)))