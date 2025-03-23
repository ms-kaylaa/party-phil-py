import discord

from commands.duderoulette import _duderoulettehandler as handler
from commands.duderoulette._duderoulettehandler import DudeRouletteRoom

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    room = handler.get_users_current_room(message.author)
    if room != None:
        if room.room_owner != message.author:
            # user is not room owner
            room.room_members.remove(message.author)
            await message.channel.send(f"You have successfully left {room.room_owner.name}'s room!")
            if len(room.room_members) == 0:
                handler.active_rooms.remove(room)
                await message.channel.send(f"{room.room_owner.name}'s room has closed because nobody's in it")
        else:
            # user is room owner
            if not room.del_confirm:    # user has not seen confirm message or a new player has recently joined the room
                room.del_confirm = True
                await message.channel.send("You are the room owner! Leaving the room will close it for everyone!\nRun `ph!leaveduderoulette` again to confirm.")
            else:
                handler.active_rooms.remove(room)
                await message.channel.send("You have successfully closed your room!")
                
    else:
        await message.channel.send("You're not in a room!")