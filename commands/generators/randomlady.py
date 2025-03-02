
import discord

from wand.image import Image
import random
from commands.generators._recolor import recolor # FUCK

async def run(msg: discord.Message,stupid1,stupid2):

    lady = recolor("lady",["#C6C0B3","#583D5F","#F3E0CB","#3F7270","#2C3F3E","#BBC9D0","#35454D"])

    await msg.reply("Here's your random lady!",file=discord.File(lady))