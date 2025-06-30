import discord
import os

from globals import USER_DIR

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    userdir = f"{USER_DIR}{str(message.author.id)}/"
    if not os.path.exists(userdir):
        os.makedirs(userdir)

    #await message.channel.send(userdir)

    attach = message.attachments

    if len(attach) == 0:
        return await message.reply("You need to attach something. I dont know what you expected from me")
    
    filename = " ".join(args)
    if "/" in filename or "\\" in filename:
        return await message.channel.send("no!")
    print(attach[0].size)

    if filename.strip() == "":
        filename = attach[0].filename
    if filename.find(".") == -1:
        filename += "." + attach[0].filename.split(".").pop()

    if filename in os.listdir(userdir):
        return await message.channel.send(f"You have already uploaded a file called {filename}. Remove it with ph!removefile {filename} or choose a different name")

    await attach[0].save(userdir + filename)
    await message.channel.send(f"Saved as {filename}")
    await message.delete()