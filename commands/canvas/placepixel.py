import discord

import userdata_handler

import re
import ast
import os
import time
import math

from PIL import Image
from PIL.Image import Resampling

rgb_regex = r'\(\d+,\s*\d+,\s*\d+\)'
xy_regex =  r'\(\d+,\s*\d+\)'

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if len(args) == 0:
        return await message.channel.send(
"""
__**PARTY PHIL CANVAS**__
 
Place a pixel by supplying two tuples (numbers contained in parentheses separated by commas): 
* Three 0-255 integers representing color *(example: (255, 108, 165))*
* Two integers, an x coordinate (0-150) and a y coordinate (0-75) *(example: (40, 22))*

You can only place a pixel once every minute and every pixel placed is subject to be overwritten by someone else. There are no claims!
*View the canvas at any time by running `ph!canvas`*
""")
    
    allowed = False

    if userdata_handler.get_data_content("lastpixel.txt", message.author).isdigit():
        timesince = math.ceil(time.time() - int(userdata_handler.get_data_content("lastpixel.txt", message.author)))
    else:
        timesince = 61
    if userdata_handler.get_data_content("lastpixel.txt", message.author) == "" or timesince > 60:
        allowed = True

    if not allowed:
        return await message.channel.send(f"You can only place a pixel once every minute. Please wait a bit before trying again. ({math.floor(60-timesince)} seconds)")

    argsraw = " ".join(args)

    rgb_str = re.findall(rgb_regex, argsraw)
    if(len(rgb_str) == 0):
        return await message.channel.send("Could not find an RGB tuple, make sure it's formatted as `(r, g, b)`")
    rgb_str = rgb_str.pop(0)

    xy_str = re.findall(xy_regex, argsraw)
    if(len(xy_str) == 0):
        return await message.channel.send("Could not find an XY tuple, make sure it's formatted as `(x, y)`")
    xy_str = xy_str.pop(0)

    rgb = ast.literal_eval(rgb_str)
    xy = ast.literal_eval(xy_str)

    # huge if statement that im not quite sure how it works
    if not all(isinstance(value, int) and 0 <= value <= 255 for value in rgb):
        return await message.channel.send("RGB values must be integers between 0 and 255")

    if not (isinstance(xy[0], int) and 0 <= xy[0] <= 150 and isinstance(xy[1], int) and 0 <= xy[1] <= 75):
        return await message.channel.send("XY coordinates must be integers: x between 0 and 150, y between 0 and 75")
    
    img = Image.open("canvas.png").convert("RGB")
    img.putpixel(xy, rgb)
    img.save("canvas.png")
    img.resize((1200, 600), Resampling.NEAREST).save("canvaspre.png")

    await message.channel.send("Successfully set pixel! You'll be able to place another in one minute.", file=discord.File("canvaspre.png"))
    with open(userdata_handler.get_data_path("lastpixel.txt", message.author), "w") as f:
        f.write(str(math.floor(time.time())))