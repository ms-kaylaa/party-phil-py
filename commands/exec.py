import discord

import globals

# exec imports
import os
import pyautogui
import pygetwindow as gw

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
                    "discord": discord, "os": os, "pyautogui": pyautogui, "gw": gw}

    exec(f"async def __exec():\n" + "\n".join(f"    {line}" for line in code.split("\n")), exec_globals)
    res = await exec_globals["__exec"]()
    try:
        await message.channel.send(res)
    except Exception as e:
        if str(e) != "400 Bad Request (error code: 50006): Cannot send an empty message": # ignore stuff that doesnt return anything
            await message.reply("I errors... `" + str(e)+"`")