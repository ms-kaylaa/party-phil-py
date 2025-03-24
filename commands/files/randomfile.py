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
    global file_list
    file_list.clear()
    if random.randint(0, 14) != 0:
        recursive_get_all_files(FILE_DIR)
    
    
        file = random.choice(file_list)
        filesplit: list[str] = file.split("/")
        owner_folder = filesplit[1]

        owner = "unknown"
        print(owner_folder)
        if owner_folder.isdigit():
            owner = client.get_user(int(owner_folder)).name
        await message.reply(f"filename: {filesplit[2]} | uploader: {owner}", file=discord.File(file))
    else:
        file_list = os.listdir("C:/sou")

        file = random.choice(file_list)

        await message.reply(f"filename: {"aaaahhh!!"} | uploader: {random.choice(["rfisk", "cara", "toreil", "asgroe"])}", file=discord.File(f"C:/sou/{file}"))