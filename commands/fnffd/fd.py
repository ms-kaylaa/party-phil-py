import discord
import globals

from websockets.sync.client import connect

async def run(message: discord.Message, args: list[str], client: discord.Client = None):

    if message.channel.id not in globals.fdtrusteds: return

    command = args[0]

    if command == "connect":
        if globals.sock != None:
            globals.sock.close()
        globals.sock = connect("ws://localhost:25565",ping_interval=None) 
        await message.reply("Connected!")

    if command == "disconnect":
        if globals.sock != None:
            globals.sock.close()
        await message.reply("Disconnected!")       
