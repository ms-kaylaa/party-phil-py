import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom


async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    targ_room = None
    for room in handler.active_rooms:
        owner = room.room_owner
        if owner.name == args[0]:
            room.room_members.append(message.author)
            await message.channel.send(f"You have joined <@{owner.id}>'s room!\n\nCurrent room members: {", ".join(member.name for member in room.room_members)}\nHost: when everybody's in, run ph!startduderoulette to begin!")