import random

async def run(message, args, client):
    await message.channel.send(random.choice(["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don’t count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]))