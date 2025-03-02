import discord

import random
import commands.generators._recolor

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    dude = "dude"
    if random.randint(0, 24) == 0:
        dude = "realdude"
    
    file = commands.generators._recolor.recolor(dude, ["#EED6C4", "#8D97C2", "#473E38", "#D7799C", "#653662", "#5F5492", "#353344"])
    await message.reply("Here's your random dude!", file=discord.File(file), mention_author=False)