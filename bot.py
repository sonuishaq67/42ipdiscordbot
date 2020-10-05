#! /usr/bin/env python3
# Python Package imports
import os
import random
import discord
from dotenv import load_dotenv
import json
import re
import sys
import time
import aiohttp
# custom tools imports
from tools.bleach import get_bleach

# create the token using the os.getenv function and the client using the discord.Client() class
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

async def fetch_data(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            return await r.json()
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

@client.event
async def on_ready():
    sys.stdout.flush()
    """
    This function will start once the bot is ready, using the client.event decorator
    and the on_ready() function. 
    It will display information about the bot itself, the server and the programmer
    """
    title = '''
     _  _     ___    __  .______    _______   __       _______.  ______   ______   .______       _______  .______     ______   .___________.
| || |   |__ \  |  | |   _  \  |       \ |  |     /       | /      | /  __  \  |   _  \     |       \ |   _  \   /  __  \  |           |
| || |_     ) | |  | |  |_)  | |  .--.  ||  |    |   (----`|  ,----'|  |  |  | |  |_)  |    |  .--.  ||  |_)  | |  |  |  | `---|  |----`
|__   _|   / /  |  | |   ___/  |  |  |  ||  |     \   \    |  |     |  |  |  | |      /     |  |  |  ||   _  <  |  |  |  |     |  |     
   | |    / /_  |  | |  |      |  '--'  ||  | .----)   |   |  `----.|  `--'  | |  |\  \----.|  '--'  ||  |_)  | |  `--'  |     |  |     
   |_|   |____| |__| | _|      |_______/ |__| |_______/     \______| \______/  | _| `._____||_______/ |______/   \______/      |__|     
                                                                                                                                        
    '''

    # bot log in information
    print('\nLogged in as {}, id: {} | Servers: {} | Users: {}'.format(client.user.name,
                                                                       client.user.id,
                                                                       len(client.guilds),
                                                                       len(set(client.get_all_members()))) + ' users')    # bot python information
    print('\nDiscord.py version: {}'.format(discord.__version__))
    # liks
    INVITE = 'PUT HERE THE LINK TO INVITE THE BOT'
    print('\nUse this link to invite {}:'.format(client.user.name))
    print(INVITE)
    REPO = 'https://github.com/sonuishaq67/42ipdiscordbot'
    print('\nGitHub repository: {}'.format(str(REPO)))
    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you all :)"))


@client.event
async def on_message(message):
    """
    This discord event is called every time the bot detects a
    message in a server
    """
    # get the channel of the bot and exit the event if the message was from the bot
    channel = client.get_channel(message.channel.id)
    if message.author == client.user:
        return

    # proccess every message
    if "what can you do" in message.content.lower():
        await channel.send('For now only 4-5 tasks {0.author.mention}'.format(message))

    elif "yoo" in message.content.lower():
        await channel.send('wassup man')

    elif "stfu bot" in message.content.lower():
        await channel.send('ok')
        sys.exit()  # turn off the bot
    elif "~latency" in message.content.lower():
        lat = await channel.send("checking...")
        print(message)
        print(lat)
        await channel.send(f"Latency: {lat.id - message.id} ms.")
    elif ("/fuck" in message.content.lower()) or ("/tf" in message.content.lower()) or ("/cringe" in message.content.lower()) or ("/eww" in message.content.lower()):
        # open the bleach.txt file
        await channel.send(f"{get_bleach('bleach.txt')}")

    elif "hi bot" in message.content.lower():
        await channel.send('Hey man {0.author.mention}'.format(message))

    elif "bot introduce yourself" in message.content:
        await channel.send("Hello @everyone I am 42ip's bot")

    elif "twss" in message.content:
        await channel.send(file=discord.File(f'assets/twss{random.randint(0, 1)}.gif'))

    elif "/noice" in message.content:
        await channel.send(file=discord.File('assets/tenor.gif'))

    elif "i love democracy" in message.content:
        await channel.send(file=discord.File('assets/democracy.gif'))

    elif "can you reply to yourself" in message.content:
        await channel.send("yes, I can")

    elif "yes i can" in message.content:
        await channel.send("oh can you reply to yourself")

    elif "toyst" in message.content.lower():
        await channel.send("https://media1.tenor.com/images/2fb6b048517ffc9492dfea5766d3835d/tenor.gif")

    elif "am i ugly" in message.content.lower():
        replies = [
            "It runs in your fam bitch",
            "Nah man you beautiful", "Yes.", "What if I told no"
        ]
        await channel.send(f'{random.choice(replies)}')

    elif "tell me a joke" in message.content.lower():
        n = random.randint(0, 2)
        if n == 2:
            joke = await fetch_data("https://official-joke-api.appspot.com/random_joke")
            await channel.send('Here\'s a joke for you')
            # await channel.send(f'{joke}')
            await channel.send(f'{str(joke["setup"])}')
            await channel.send(f'{str(joke["punchline"])}')

        elif n == 1:
            await channel.send('Your life')

        else:
            await channel.send('Sorry I cant open your front camera yet')
    elif "~ping" in message.content.lower():
        os.system("ping google.com -c 1 1>ping")
        with open('ping') as pingfile:
            for line in nonblank_lines(pingfile):
                await channel.send(f'{line}')
    elif "r! meme" in message.content.lower():
        subreds = ["memes", "dankmemes", "programmerhumor", "boneappletea", "funny",
                   "cursedcomments", "linuxmemes", "interestingasfuck", "murderedbywords"]
        n = subreds[random.randint(0, len(subreds)-1)]
        # get the meme
        meme = await fetch_data(f"https://meme-api.herokuapp.com/gimme/{n}")
        print(meme)
        await channel.send(f'**{str(meme["title"])}** from *{str(meme["subreddit"])}*')
        await channel.send(f'{str(meme["url"])}')

if __name__ == '__main__':
    sys.stdout.flush()
    client.run(TOKEN)
