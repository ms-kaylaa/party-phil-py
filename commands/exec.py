import discord

import globals
import re

# exec imports
import os
import pyautogui
import pygetwindow as gw
import lupa

async def run(message: discord.Message, args, client: discord.Client):
    #return
    if str(message.author.id) not in globals.trusteds and not message.author.id == 1135951334651207701:
        print("denied")
        return
    
    if message.content.__contains__("token") : #or message.content.__contains__("press") or message.content.__contains__("keyDown") or message.content.__contains__("type")
        await message.reply("fuck off")
        return
    
    if message.content.__contains__(".title"): return

    code = " ".join(args)
    exec_globals = {"message": message, "client": client, 
                    "discord": discord, "os": os, "pyautogui": pyautogui, "gw": gw, "lupa": lupa, "hawk": "tuah"}

    exec(f"async def __exec():\n" + "\n".join(f"    {line}" for line in code.split("\n")), exec_globals)
    res = await exec_globals["__exec"]()
    try:
        res = str(str(res))

        exclude_paths = [
            os.getcwd(),
            os.environ["APPDATA"],
            os.environ["LOCALAPPDATA"]
        ]

        for path in exclude_paths:
            escaped_path = re.escape(path.replace("\\", "\\\\"))
            res = re.sub(escaped_path, "PHIL", res, flags=re.IGNORECASE)

        await message.channel.send(res)
    except Exception as e:
        if str(e) != "400 Bad Request (error code: 50006): Cannot send an empty message": # ignore stuff that doesnt return anything
            await message.reply("I errors... `" + str(e)+"`")