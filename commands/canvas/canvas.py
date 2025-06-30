import discord

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    await message.channel.send("here's the current canvas", file=discord.File("canvaspre.png"))