import discord
import globals

import pyautogui

from websockets.sync.client import connect

async def run(message: discord.Message, args: list[str], client: discord.Client = None):

    if message.channel.id not in globals.fdtrusteds: return

    if len(args) == 0 or args[0] == "help":
        await message.channel.send(
"""**__FREECONNECT24 COMMANDS__**:

**SETUP**
* `connect`: Attempt to establish a connection with the FreeConnect24 server running on the host machine.
* `disconnect`: Attempt to close an already existing connection with the FreeConnect24 server running on the host machine.

**VISUAL**
* `ntsc`: Toggle the NTSC filter in songs.
* `wavey`: Toggle the wavey effect used in starfire.

* `hideui`: Hide the ui note visibility for 7 seconds.
* `flipnotes`: Flip the note surface, effectively enabling downscroll.

**GAMEPLAY**
* `increasepitch`: Increase the song pitch/speed.
* `decreasepitch`: Decrease the song pitch/speed.

* `pause`: Acts as though enter was pressed.

* `healthdrain`: Enables opponent health drain (a la Buddy in Twinkle or CD Boy in Tsunami).
* `yousuck`: Sets flow to 0.

**MODCHART**
* `notewave`: Makes the notes move in a wavelike pattern for 15 seconds. Stacks and resets timer if used multiple times.
* `drunk`: Makes the notes move unpredictably. Stacks and resets timer if used multiple times.
""")
        return
    command = args[0]

    if command == "connect":
        if globals.sock != None:
            globals.sock.close()
        globals.connected_channel_id = message.channel.id
        globals.sock = connect("ws://localhost:25565",ping_interval=None) 
        # send channel title to show up
        globals.sock.send(message.channel.name, True)
        await message.reply("Connected!")

    if command == "disconnect":
        if globals.sock != None:
            globals.sock.close()
            globals.sock = None
            globals.connected_channel_id = 0
        await message.reply("Disconnected!")    
