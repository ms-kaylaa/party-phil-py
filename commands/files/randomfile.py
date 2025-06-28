import discord

import os
import random

from globals import FILE_DIR

import stat_handler

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
    stat_handler.stats["command_stats"]["files_gotten"] += 1
    if random.randint(0, 14) != 0:
        err_res = ""
        if len(args) >= 1:
            # get files from a user
            ids = []
            skipped = []
            users = client.get_all_members()
            for arg in args:
                user = None
                for userr in users:
                    if userr.name == arg:
                        user = userr
                        break
                if user == None or not os.path.isdir(f"filedb/{user.id}"):
                    skipped.append(arg)
                    continue
                
                ids.append(user.id)

            if len(skipped) > 0:
                err_res += f"Skipped the following users: {", ".join(skipped)}"

            file_list = []
            for id in ids:
                for file in os.listdir(f"filedb/{id}"):
                    file_list.append(f"filedb/{id}/{file}")
        if len(file_list) == 0:
            if len(args) > 0:
                err_res += "\nNone of the selected users were valid; defaulting to normal file distribution"
            recursive_get_all_files(FILE_DIR)
        if err_res != "":
            await message.channel.send(err_res)
    
        file = random.choice(file_list)
        filesplit: list[str] = file.split("/")
        owner_folder = filesplit[1]

        owner = "unknown"
        owner_attr = "unknown"
        print(owner_folder)
        if owner_folder.isdigit():
            owner = client.get_user(int(owner_folder))
            owner_attr = f"{owner.display_name} ({owner.name})"
        print(file)
        await message.reply(f"filename: {filesplit[2]} | uploader: {owner_attr}", file=discord.File(file))
    else:
        file_list = os.listdir("C:/sou")
        stat_handler.stats["command_stats"]["story_of_undertale_rolls"] += 1

        file = random.choice(file_list)

        await message.reply(f"filename: {"aaaahhh!!"} | uploader: {random.choice(["rfisk", "cara", "toreil", "asgroe"])}", file=discord.File(f"C:/sou/{file}"))