import json

stats = {}

def load_stats():
    global stats
    with open("STATS.json") as f:
        stats = json.loads(f.read())
def save_stats():
    global stats
    with open("STATS.json", 'w') as f:
        f.write(json.dumps(stats))

def get_stat(stat:str):
    return stats[stat]
# it needs to constantly save so that if i just shut him down he will retain memory
def increment_stat(stat:str, amt:int=1):
    set_stat(stat, stats[stat]+amt)
    save_stats()
def set_stat(stat:str, value):
    stats[stat] = value
    save_stats()