import discord

import os

from globals import FILE_DIR
import stat_handler

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
    global file_list

    file_list.clear()
    recursive_get_all_files(FILE_DIR)
    filename = " ".join(args)

    found_indices: list[str] = []
    for i in range(len(file_list)):
        file = file_list[i]

        end = file.split("/").pop()
        if end == filename:
            #await message.channel.send("i found it: " + str(i))
            print(i, file_list[i])
            found_indices.append(i)

    if len(found_indices) > 0:
        stat_handler.stats["command_stats"]["files_gotten"] += 1
        if len(found_indices) > 1:
            await message.reply("i found multiple uploads with that name")
        for found_index in found_indices:
            owner_folder = file_list[found_index].split("/")[1]

            owner = "unknown"
            owner_attr = "unknown"
            if owner_folder.isdigit():
                owner = client.get_user(int(owner_folder))
                owner_attr = f"{owner.display_name} ({owner.name})"
            await message.reply(f"uploader: {owner_attr}", file=discord.File(file_list[found_index]))
    else:
        await message.reply("i didnt find i t...")