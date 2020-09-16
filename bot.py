import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    print(message)
    channel = client.get_channel(message.channel.id)
    if message.author == client.user:
        return

    if "what can you do" in message.content:
        msg = 'For now only 4-5 tasks {0.author.mention}'.format(message)
        await channel.send(f'{msg}')
    elif "hi bot" in message.content:
        await channel.send('Hey man {0.author.mention}'.format(message))
    elif "introduce yourself" in message.content:
        msg = "Hello @everyone I am 42ip's bot"
        await channel.send(f'{msg}')
    elif "twss" in message.content:
        i = random.randint(0,1)
        await channel.send(file=discord.File(f'assets/twss{i}.gif'))
    elif "noice" in message.content:
        await channel.send(file=discord.File('assets/tenor.gif'))
    elif "i love democracy" in message.content:
        await channel.send(file=discord.File('assets/democracy.gif'))
    elif "can you reply to yourself" in message.content:
        msg = 'yes i can'
        await channel.send(f'{msg}')
    elif "yes i can" in message.content:
        msg = "oh can you reply to yourself"
        await channel.send(f'{msg}')
    elif "am i ugly" in message.content.lower():
        replies = ["It runs in your fam bitch",
                   "Nah man you beautiful", "Yes.", "What if I told no"]
        n = random.randint(0, len(replies)-1)
        await channel.send(f'{replies[n]}')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
