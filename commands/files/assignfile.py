import discord

from globals import trusteds

import os

async def run(message: discord.Message, argsraw: list[str], client: discord.Client = None):
    if not str(message.author.id) in trusteds:
        users = []
        for trusted in trusteds:
            users.append(client.get_user(int(trusted)).name)
        await message.channel.send(f"you are not allowed to perform that command!\ncontact one of the approved users ({", ".join(users)}) to reassign it! (or contact kayla to add you as a trusted user)")
        return
    if argsraw[0] == "list":
        await message.channel.send(os.listdir("filedb/pre-refactor files"))
        return
    args = " ".join(argsraw)
    args = args.split("\" ")
    args[0] = args[0][1:]
    if len(args) != 2:
        return await message.channel.send("syntax: ph!assignfile \"filename.ext\" username (e.g. .hexose., ms_kaylaa)")
    if not args[0] in os.listdir("filedb/pre-refactor files"):
        return await message.channel.send("that file doesnt exist or you typed it wrong. make sure to include the extension")
    
    # no error handling cause this is backend
    id = -1
    for user in client.get_all_members():
        if user.name == args[1]:
            id = user.id
            break

    if id != -1:
        if not os.path.exists(f"filedb/{id}"):
            os.makedirs(f"filedb/{id}")
        os.rename(f"filedb/pre-refactor files/{args[0]}", f"filedb/{id}/{args[0]}")

        await message.channel.send("successfully moved file!!")
    else:
        await message.channel.send("couldnt find that user sorry pal")