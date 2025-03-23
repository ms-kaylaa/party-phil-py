import discord

from sync import load_commands, commands_dict
from commands.duderoulette import _duderoulettehandler as drhandler

import random
import traceback

import os

prefix = "ph!"
class Phil(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Wii Party"))
        load_commands()
        #test_commands(self)

    async def on_message(self, message: discord.Message):
        if message.author.bot or not message.content.lower().startswith(prefix): return
        
        if random.randint(0, 23) == 9: # the one constant of party phil
            await message.channel.send("Fuck you! 👎")
            return
        
        await handle_commands(self, message)
        await drhandler.duderoulette_onmessage(self, message)
        
async def handle_commands(self: Phil, message: discord.Message):
    # this is kinda a dumb way to do it
    split = message.content.split(prefix)
    split.pop(0) # remove prefix split
        
    args = "".join(split).split(" ") # This is good
    command = args.pop(0)

    print(command, args)
    if command in commands_dict:
        try:
            await commands_dict[command].run(message, args, self)
        except Exception as e:
            await message.reply("I errors... " + str(e))
            traceback.print_exception(e)

def read_token():
    f = open("token.txt")

    for line in f.readlines():
        if not line.startswith("#"):
            return line
        
    return "oops"

# TODO
def test_commands(client: discord.Client):
    print(client.get_channel(1345163896008343634).name)
    for root, _, files in os.walk("./commands"):
        for file in files:
            file_path = os.path.join(root, file)
            if not "__pycache__" in root:
                print(root)
    pass


intents = discord.Intents.all() # IM LAZY TODO ACTUAL INTENTS

client = Phil(intents=intents)
client.run(read_token())