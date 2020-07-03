# made following https://realpython.com/how-to-make-a-discord-bot-python/
# except ignoring any parts where they wrote code

import os
import random
import json

import requests
import discord

#discord auth
token = "token here"
guild = "name of server here" # doesn't seem to do anything?

#imgflip auth
username = "imgflip username here"
password = "imgflip password here"

client = discord.Client()

def makememe(user, text):
    meme = random.choice(["163573", "13757816", "1367068"])
    url = "https://api.imgflip.com/caption_image"
    content = {
        "template_id": meme,
        "username": username,
        "password": password,
        "text0": f"{user} said:",
        "text1": text,
    }

    r = requests.post(url, content)
    c = json.loads(r.content)
    return c["data"]["url"]


@client.event
async def on_message(message):
    if random.randint(1, 10) > 7:
        return
    if message.author == client.user:
        return
    if str(message.channel) not in ['another-channel', 'robot-prison']:
        return
    else:
        user = str(message.author).split("#")[0]
        content = message.content
        meme = makememe(user, content)
        await message.channel.send(meme)

client.run(token)