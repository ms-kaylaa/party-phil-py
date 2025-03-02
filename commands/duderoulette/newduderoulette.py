import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if handler.get_users_current_room(message.author) == None:
        handler.active_rooms.append(DudeRouletteRoom(message))
        await message.channel.send("yeeep... ur in a room now pal")
    else:
        await message.channel.send("You're already in a room!")