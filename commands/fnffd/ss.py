import discord
import pyautogui
import pygetwindow as gw

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if gw.getActiveWindow().title != "Created with GameMaker" and gw.getActiveWindow().title != "FNF FREE DOWNLOAD":
        return await message.channel.send("kayla is not currently tabbed into fnffd")
    ss = pyautogui.screenshot()
    ss = ss.crop((1920//2-1300//2, 1080//2-800//2, 1920//2+1300//2, 1080//2+800//2))
    ss.save("ss.png")
    await message.channel.send(file=discord.File("ss.png"))