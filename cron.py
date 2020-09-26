import os
import random
import discord
from dotenv import load_dotenv
import requests
import json
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = client.get_channel(744840774759481345)
    subreds = ["memes","dankmemes","programmerhumor","boneappletea","funny"
    n = subreds[random.randint(0,len(subreds)-1)]
    response = requests.get(f"https://meme-api.herokuapp.com/gimme/{n}")
    meme = response.json()
    print(meme)
    await channel.send(f'**{str(meme["title"])}**  from *{str(meme["subreddit"])}*')
    await channel.send(f'{str(meme["url"])}')
    exit()

client.run(TOKEN)
