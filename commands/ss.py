import discord
import pyautogui

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    return await message.reply("until next time!")
    ss = pyautogui.screenshot()
    ss = ss.crop((1920//2-400, 1080//2-400, 1920//2+400, 1080//2+400))
    ss.save("ss.png")
    await message.channel.send(file=discord.File("ss.png"))