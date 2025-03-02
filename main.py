import discord

from sync import load_commands, commands_dict

import random
import traceback

import os
import globals

import websockets

def read_token():
    f = open("token.txt")

    for line in f.readlines():
        if not line.startswith("#"):
            return line
        
    return "oops"

def test_commands(client: discord.Client):
    print(client.get_channel(1345163896008343634).name)
    for root, _, files in os.walk("./commands"):
        for file in files:
            file_path = os.path.join(root, file)
            if not "__pycache__" in root:
                print(root)
    pass

prefix = "ph!"
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Wii Party"))
        load_commands()
        #test_commands(self)

    async def on_message(self, message: discord.Message):
        send_content_to_socket = False
        if globals.sock != None and not message.author.bot and message.channel.id in globals.fdtrusteds:
            print("marking content for sending")
            send_content_to_socket = True
        if message.author.bot or (not message.content.lower().startswith(prefix) and not send_content_to_socket): return
        if random.randint(0, 23) == 9 and message.content.lower().startswith(prefix):
            await message.channel.send("Fuck you! 👎")
            send_content_to_socket = False
            return

        if send_content_to_socket:
            print("sending")
            try:
                globals.sock.send(f"[{message.author}]: {message.content}",text=True) # commands are done from gamemaker!!   
            except websockets.exceptions.ConnectionClosedError:
                globals.sock.close()
                globals.sock = None
                await message.channel.send("i lost connection to the freeconnect server!")

        # this is kinda a dumb way to do it
        split = message.content.split(prefix)
        split.pop(0) # remove prefix split
        
        # merge... to split again.
        merged = ""
        for s in split:
            merged += s
        
        args = merged.split(" ") # This is good
        command = args.pop(0)

        print(command, args)
        if command in commands_dict:
            try:
                await commands_dict[command].run(message, args, self)
            except Exception as e:
                await message.reply("I errors... " + str(e))
                traceback.print_exception(e)


intents = discord.Intents.all() # IM LAZY TODO ACTUAL INTENTS

client = MyClient(intents=intents)
client.run(read_token())