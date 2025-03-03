import discord
import globals

import pyautogui

from websockets.sync.client import connect

async def run(message: discord.Message, args: list[str], client: discord.Client = None):

    if message.channel.id not in globals.fdtrusteds: return

    if len(args) == 0:
        await message.channel.send(
"""**__FREECONNECT24 COMMANDS__**:

**SETUP**
`connect`: Attempt to establish a connection with the FreeConnect24 server running on the host machine.
`disconnect`: Attempt to close an already existing connection with the FreeConnect24 server running on the host machine.

**GAMEPLAY**
`ntsc`: Toggle the NTSC filter in songs.
`wavey`: (BROKEN) Toggle the wavey effect used in starfire.

`hideui`: Hide the ui note visibility for 7 seconds.

`increasepitch`: Increase the song pitch/speed.
`decreasepitch`: Decrease the song pitch/speed.
""")
        return
    command = args[0]

    if command == "connect":
        if globals.sock != None:
            globals.sock.close()
        globals.sock = connect("ws://localhost:25565",ping_interval=None) 
        await message.reply("Connected!")

    if command == "disconnect":
        if globals.sock != None:
            globals.sock.close()
            globals.sock = None
        await message.reply("Disconnected!")    
