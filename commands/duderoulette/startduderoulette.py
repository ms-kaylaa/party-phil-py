import discord

from commands.duderoulette import _duderoulettehandler as handler

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    room = handler.get_users_current_room(message.author)
    if room != None and room.room_owner == message.author:
        await message.channel.send("Ok i acknowledge that you want to start the room and are the room owner\nUnfortunately that doesnt exist yet sorry")
    else:
        await message.channel.send("You are either not in a room or are not the owner of the room you are in!")