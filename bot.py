import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    channel = client.get_channel(714036401334911036)
    if message.author == client.user:
        return

    if "what can you do" in message.content:
        msg = 'Hello {0.author.mention}'.format(message)
        await channel.send(f'{msg}')
    if "introduce yourself" in message.content:
        msg = 'Hello @everyone I am java.awt'
        await channel.send(f'{msg}')
    if "noice" in message.content:
        await channel.send('Hello', file=discord.File('tenor.gif'))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
