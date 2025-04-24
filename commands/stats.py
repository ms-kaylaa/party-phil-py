import discord
import os

from globals import FILE_DIR
import stat_handler

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    file_list = []
    def recursive_get_files(dir):
        for file in os.listdir(dir):
            #await msg.channel.send(file)
            if os.path.isdir(dir + file + "/"):
                #await msg.channel.send("entered this dir ^")
                recursive_get_files(dir + file + "/")
                #await msg.channel.send("exited dir " + dir)
            else:
                file_list.append(dir + file)
    
    recursive_get_files(FILE_DIR)
    await message.channel.send(
f"""
__***GENERAL STATS***__
**Commands run**: {stat_handler.get_stat("commands_run")}
**Errors**: {stat_handler.get_stat("errors")}
**"Fuck you! 👎"s**: {stat_handler.get_stat("fuck_yous")}

__***COMMAND STATS***__
**Dudes generated**: {stat_handler.stats["command_stats"]["dudes_generated"]}
**Files gotten**: {stat_handler.stats["command_stats"]["files_gotten"]}

__***MISC***__
**Total files uploaded**: {len(file_list)}
**Story of Undertale rolls**: {stat_handler.stats["command_stats"]["story_of_undertale_rolls"]}
""")