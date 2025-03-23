import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if not handler.user_is_in_room(message.author):
        handler.active_rooms.append(DudeRouletteRoom(message))
        await message.channel.send(f"You have successfully made a Dude Roulette room!\nOthers can join your room by running `ph!joinduderoulette {message.author.name}")
    else:
        await message.channel.send("You're already in a room!")