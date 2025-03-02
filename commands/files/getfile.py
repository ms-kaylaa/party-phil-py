import discord

import os

from globals import FILE_DIR

file_list: list[str] = []
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
    filename = " ".join(args)

    found_index = -1
    for i in range(len(file_list)):
        file = file_list[i]

        end = file.split("/").pop()
        if end == filename:
            #await message.channel.send("i found it: " + str(i))
            found_index = i
            break

    if found_index != -1:
        await message.reply(file=discord.File(file_list[found_index]))
    else:
        await message.reply("i didnt find i t...")