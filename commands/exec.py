import discord

# exec imports
import os

allowed_users = [
    1135951334651207701, # me
    587298000439869463, # hexose
    605229752995020800 # jc
]
async def run(message: discord.Message, args, client: discord.Client):
    if message.author.id not in allowed_users:
        print("denied")
        return
    
    if message.content.__contains__("token"):
        await message.reply("fuck off")
        return

    code = " ".join(args)
    exec_globals = {"message": message, "client": client, "discord": discord, "os": os}

    exec(f"async def __exec():\n" + "\n".join(f"    {line}" for line in code.split("\n")), exec_globals)
    res = await exec_globals["__exec"]()
    try:
        await message.channel.send(res)
    except Exception as e:
        if str(e) != "400 Bad Request (error code: 50006): Cannot send an empty message": # ignore stuff that doesnt return anything
            await message.reply("I errors... " + str(e))