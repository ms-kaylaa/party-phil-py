# holds info about current dude roulette game
# rules courtesy of riq: https://docs.google.com/document/d/1MYQduO5Osz1UhPzm7gYJU7eKHQjpaniKSjsaAf6werQ/edit?tab=t.0

import discord

class DudeRouletteRoom():
    def __init__(self, creation_message: discord.Message):
        self.creation_message: discord.Message = creation_message
        self.room_owner: discord.User = self.creation_message.author
        self.room_guild: discord.Guild = self.creation_message.guild 

        self.game_started = False
        self.room_members: list[discord.Member] = [self.room_owner]


active_rooms: list[DudeRouletteRoom] = []

def get_users_current_room(user: discord.Member) -> DudeRouletteRoom:
    for room in active_rooms:
        if user in room.room_members:
            return room
        
    return None