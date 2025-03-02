import discord
import os

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    userdir = f"filedb/{str(message.author.id)}/"
    if not os.path.exists(userdir):
        os.makedirs(userdir)

    #await message.channel.send(userdir)

    attach = message.attachments

    if len(attach) == 0:
        await message.reply("temp reply (you need to attach shit)")
        return
    
    filename = " ".join(args)

    await attach[0].save(userdir + filename)
    await message.channel.send(f"temp success (saved {filename})")
    await message.delete()