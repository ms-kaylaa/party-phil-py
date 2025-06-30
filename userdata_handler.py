import discord

import os
from globals import USER_DIR

def get_data_path(filename:str, user:discord.User):
    path = f"{USER_DIR}{user.id}/data/{filename}"
    if not os.path.exists(path):
        if not os.path.exists(f"{USER_DIR}{user.id}/data"):
            os.makedirs(f"{USER_DIR}{user.id}/data")
        with open(path, "w") as f:
            f.write("")
    return path

def get_data_content(filename:str, user:discord.User):
    path = get_data_path(filename, user)

    with open(path) as f:
        content = f.read()
    return content