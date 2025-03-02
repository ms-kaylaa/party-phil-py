import discord

import compileallfixed
import importlib
import os

commands_dict = {}

def load_commands():
    commands_dict.clear()
    base_path = "commands"
    base_prefix = len(base_path) + 1  # get the index where stuff we care about shows up (end of "commands/")
    
    for root, _, files in os.walk(base_path):
        relative_root = root[base_prefix:].replace(os.sep, ".")  # convert to module path
        if relative_root.startswith("_") or relative_root.endswith("_"):
            continue  # skip backend stuff
        
        for file in files:
            if not file.endswith(".py") or file.startswith("_"):
                continue  # skip backend stuff
            
            name = file[:-3]  # remove extension
            module_path = f"commands.{relative_root + '.' if relative_root else ''}{name}"
            commands_dict[name] = importlib.import_module(module_path)
            print(f"loaded: {module_path}")

# louder cooler but probably slower
async def sync(message: discord.Message):
    await message.channel.send("syncing commands...")
    
    recompiled = 0
    added = 0
    removed = 0

    base_path = "commands"
    base_prefix = len(base_path) + 1
    
    for root, _, files in os.walk(base_path):
        relative_root = root[base_prefix:].replace(os.sep, ".")
        
        for file in files:
            valid_command = True
            silent = False
            if not file.endswith(".py") or file.startswith("_") or relative_root.endswith("_"):
                silent = True # mute backend stuff
                valid_command = False
            
            name = file[:-3]
            module_path = f"commands.{relative_root + '.' if relative_root else ''}{name}"
            
            # add new commands
            if name not in commands_dict and valid_command:
                if not silent:
                    await message.channel.send(f"added: {name}")
                    added+=1
                commands_dict[name] = importlib.import_module(module_path)
            
            # recompile old commands
            compiled = compileallfixed.compile_file(os.path.join(root, file), quiet=True) # returns true if it changed and false if it didnt. i had to make this functionality myself. fuck.
            if compiled and valid_command:
                recompiled+=1
                await message.channel.send(f"recompiled: {name}")
    # look for removed commands
    removedcmds = []
    for key, module in list(commands_dict.items()):
        try:
            commands_dict[key] = importlib.reload(module)
        except ModuleNotFoundError:
            removedcmds.append(key)
            await message.channel.send(f"removed: {key}")
            removed+=1
    
    # remove commands marked for removal
    for key in removedcmds:
        del commands_dict[key]

    await message.channel.send(f"im done syncing! recompiled: {recompiled}, added: {added}, removed: {removed}")

# probably faster no-output version of sync
def silentsync():
    compileallfixed.compile_dir("commands/", quiet=True)
    
    # look for and remove commands
    for key, module in list(commands_dict.items()):
        try:
            commands_dict[key] = importlib.reload(module)
        except ModuleNotFoundError:
            del commands_dict[key]
    
    for root, _, files in os.walk("commands"):  
        relative_root = root[9:].replace(os.sep, ".")  
        if relative_root.endswith("_"):
            continue # skip backend stuff
        
        for file in files:
            if not file.endswith(".py") or file.startswith("_"):
                continue # skip backend stuff
            
            name = file[:-3] # remove extension. also :-3
            module_path = f"commands.{relative_root + '.' if relative_root else ''}{name}" # get proper module name
            
            # add new commands
            if name not in commands_dict:
                commands_dict[name] = importlib.import_module(module_path)
