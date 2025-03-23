import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom


async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if len(args) == 0:
        return await message.channel.send("You need to specify the owner of the room you'd like to join!")
    if handler.user_is_in_room(message.author):
        return await message.channel.send("You're already in a room!")
    
    found_room = False
    for room in handler.active_rooms:
        owner = room.room_owner
        if owner.name == args[0] and room.room_guild == message.guild:
            found_room = True
            if not room.game_started:
                room.room_members.append(message.author)
                room.del_confirm = False    # reset "are you sure"
                await message.channel.send(f"You have joined {owner.name}'s room!\n\nCurrent room members: {", ".join(member.name for member in room.room_members)}\nHost: when everybody's in, run ph!startduderoulette to begin!")
            else:
                await message.channel.send("That game has already started!")

            break

    if not found_room and not handler.user_is_in_room(message.author):
        # they didnt join a room so their search failed. rip!
        await message.channel.send("I couldn't find a room in this server owned by someone with that username!")