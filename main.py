import discord

import stat_handler
from sync import load_commands, commands_dict
from commands.duderoulette import _duderoulettehandler as drhandler

import random
import traceback

import os

PREFIX = "ph!"
class Phil(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Wii Party"))
        load_commands()
        stat_handler.load_stats()
        #test_commands(self)

    async def on_message(self, message: discord.Message):
        await handle_stats(self,message)
        if "<@1141102885472587777>" in message.content and not message.content.lower().startswith(PREFIX):
            await message.channel.send("my name party phil")
        if (message.author.bot and not message.author.id == 1338550487414214717) or not message.content.lower().startswith(PREFIX): return
        
        if not message.content.startswith("ph!addfile") and random.randint(0, 41) == 9: # the one constant of party phil
            await message.channel.send("Fuck you! 👎")
            stat_handler.increment_stat("fuck_yous")
            return
        
        await handle_commands(self, message)
        await drhandler.duderoulette_onmessage(self, message)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # smiley react
        if payload.channel_id == 1220096882223743077:
            allowed_smiles = [1213981788322668595, 1213976609221115904, 1225198377755611177, 1213976689499963442, 1213976726791651399, 1225199725419036802, 1225198374064619571, 1213977580978577458, 1213976671385026570, 1225199726325137408, 1225199728720085043, 1223739074590933112, 1225199730070519890]
            msg: discord.Message = await self.get_guild(payload.guild_id).get_channel(payload.channel_id).fetch_message(payload.message_id)

            score = 0
            for reaction in msg.reactions:
                if reaction.emoji.id in allowed_smiles or reaction.emoji.name.startswith("spr_ladyfont_"):
                    score += reaction.count
            
            if score > stat_handler.get_stat("highest_smiley_reaction_score"):
                stat_handler.set_stat("highest_smiley_reaction_score", score)
                await msg.channel.edit(topic=f"only happy here\nyes yes! | current streak: {stat_handler.get_stat("current_smiley_streak")}, longest streak: {stat_handler.get_stat("longest_smiley_streak")}, highest reaction score: {stat_handler.get_stat("highest_smiley_reaction_score")}")
        
async def handle_commands(self: Phil, message: discord.Message):
    # this is kinda a dumb way to do it
    split = message.content.split(PREFIX)
    split.pop(0) # remove prefix split
        
    args = PREFIX.join(split).split(" ") # This is good
    command = args.pop(0)

    print(command, args)
    if command in commands_dict:
        stat_handler.increment_stat("commands_run")
        try:
            await commands_dict[command].run(message, args, self)
        except Exception as e:
            await message.reply("I errors... `" + str(e)+"`")
            stat_handler.increment_stat("errors")
            traceback.print_exception(e)

async def handle_stats(self:Phil, message:discord.Message):
    if message.author.bot:
        return
    # smiley stat
    allowed_smiles = ["<:spr_smiley_0:1213981788322668595>", "<:evil:1213976609221115904>", "<:hislick:1225198377755611177>", "<:spr_dudeicon_0:1213976689499963442>", "<:spr_momgotmcdonalds_0:1213976726791651399>", "<:KillChildren:1225199725419036802>", "<:dalethumbs:1225198374064619571>", "<:snd_own:1213977580978577458>", "<:snd_win:1213976671385026570>", "<:spr_crazyjohnny_0:1225199726325137408>", "<:sun:1225199728720085043>", "<:stradballin:1223739074590933112>", "<:isaidfunkin:1225199730070519890>"]
    if message.channel.id == 1220096882223743077:
        if (message.content.strip() in allowed_smiles or message.content.strip().startswith("<:spr_ladyfont_")):
            if message.author.id != stat_handler.get_stat("last_smiley_id"):
                stat_handler.set_stat("last_smiley_id", message.author.id)

                stat_handler.increment_stat("current_smiley_streak")
                if stat_handler.get_stat("current_smiley_streak") > stat_handler.get_stat("longest_smiley_streak"):
                    stat_handler.set_stat("longest_smiley_streak", stat_handler.get_stat("current_smiley_streak"))
        elif message.content.strip().startswith("<:") or (len(message.content.strip()) == 0 and len(message.attachments) > 0) or message.content.strip().startswith(":"):
            # gray area
            pass
        else:
            # fucked up!
            stat_handler.set_stat("last_smiley_id", message.author.id)
            stat_handler.set_stat("current_smiley_streak", 0)

            await message.channel.send("ohhhh oh the streak just got reset ohhhhhhhhhhhh nooooo")

        await message.channel.edit(topic=f"only happy here\nyes yes! | current streak: {stat_handler.get_stat("current_smiley_streak")}, longest streak: {stat_handler.get_stat("longest_smiley_streak")}, highest reaction score: {stat_handler.get_stat("highest_smiley_reaction_score")}")

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