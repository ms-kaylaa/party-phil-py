import discord

import os

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if len(args) < 1:
        args.append(message.author.name)

    id = 0
    for user in client.get_all_members():
        if user.name == args[0]:
            id = user.id

    if id == 0:
        return await message.channel.send("That user has no uploaded files")
    
    return await message.channel.send(f"{client.get_user(id).name}'s files\n{", ".join(os.listdir(f"filedb/{id}"))}")

    