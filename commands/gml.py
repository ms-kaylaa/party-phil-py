import discord

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    return await message.reply("until next time!")
    for arg in args:
        if "game_" in arg or "room_" in arg or "live_" in arg:
            await message.reply("no")
            return
    with open("gml.txt", 'w') as f:
        f.write(" ".join(args))