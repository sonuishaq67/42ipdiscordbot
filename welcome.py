import os
import random
import discord
from dotenv import load_dotenv
import requests
import json
import re
import sys
import time
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
@client.event
async def on_member_join(client, *, member):
    channel = client.get_channel(714036401334911036)
    time.sleep(600)
    fmt = '@everyone {member.name} is here!'
    await channel.send(f'{fmt}')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
