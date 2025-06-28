import discord
import sys
import time
import random

import stat_handler

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    await message.channel.send("IM DELETING YOU, `party phil` !😭👋 ")
    stat_handler.save_stats()
    time.sleep(1)
    msg = await message.channel.send(content="██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete...")
    time.sleep(random.random()*2+1)
    await msg.edit(content="████]]]]]]]]]]]]]]]]]]]]]]] 35% complete...")
    time.sleep(random.random()*2+1)
    await msg.edit(content="███████]]]]]]]]]]]]]] 60% complete...")
    time.sleep(random.random()*2+1)
    await msg.edit(content="███████████] 99% complete...")
    time.sleep(random.random()*2+1)
    await msg.edit(content="████████████100%")

    if random.random() < .5:
        raise Exception("🚫ERROR!🚫 ❣️party phil❣️💯 is forever")
    else:
        await message.channel.send("Self destructing")
        sys.exit(0)