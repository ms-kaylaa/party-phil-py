import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    room = handler.get_users_current_room(message.author)
    if room != None:
        room.room_members.remove(message.author)
        await message.channel.send("yeeep... ur no longer in a room now pal")
        if len(room.room_members) == 0:
            handler.active_rooms.remove(room)
            await message.channel.send(f"<@{room.room_owner.id}>'s room has closed because nobody's in it")
    else:
        await message.channel.send("You're not in a room!")