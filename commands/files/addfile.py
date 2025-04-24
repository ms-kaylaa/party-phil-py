import discord
import os

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    userdir = f"filedb/{str(message.author.id)}/"
    if not os.path.exists(userdir):
        os.makedirs(userdir)

    #await message.channel.send(userdir)

    attach = message.attachments

    if len(attach) == 0:
        await message.reply("You need to attach something. I dont know what you expected from me")
        return
    
    filename = " ".join(args)
    print(attach[0].size)

    await attach[0].save(userdir + filename)
    await message.channel.send(f"Saved as {filename}")
    await message.delete()