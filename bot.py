#!/usr/bin/python3
# Python Package imports
import os
import random
import discord
from dotenv import load_dotenv
import json
import re
import sys
import time
import time
import calendar
import requests
from customdefs import *
# custom tools imports
from tools.bleach import get_bleach

# create the token using the os.getenv function and the client using the discord.Client() class
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()



@client.event
async def on_ready():
    x=random.randint(0,2)
    status=getstatus()
    activity=discord.Activity(type=gettype(x),name=getname(x))
    await client.change_presence(status=status,activity=activity)


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
    print(message)
    print(message.content)
    # proccess every message
    if "what can you do" in message.content.lower():
        await channel.send('For now only 4-5 tasks {0.author.mention}'.format(message))

    elif message.content.startswith("/doge"):
        api_url = "http://shibe.online/api/shibes?count=1"
        response = await fetch_data(api_url)
        embed = discord.Embed(
            title=f"doge for {message.author}",
        )
        embed.set_image(url=f"{response[0]}")
        await channel.send(embed=embed)

    elif "~latency" in message.content.lower():
        lat = await channel.send("checking...")
        latutc = sf2utcms(lat.id)
        msutc = sf2utcms(message.id)
        await channel.send(f"Latency: {latutc-msutc} ms.")
    elif ("/fuck" in message.content.lower()) or ("/tf" in message.content.lower()) or ("/cringe" in message.content.lower()) or ("/eww" in message.content.lower()):
        # open the bleach.txt file
        await channel.send(url=f"{get_bleach('bleach.txt')}")

    elif "hi bot" in message.content.lower():
        await channel.send('Hey man {0.author.mention}'.format(message))

    elif "bot introduce yourself" in message.content:
        await channel.send("Hello @everyone I am 42ip's bot")

    elif "twss" in message.content:
        await channel.send(file=discord.File(f'assets/twss{random.randint(0, 1)}.gif'))

    elif "/noice" in message.content:
        await channel.send(file=discord.File('assets/tenor.gif'))

    elif message.content.startswith('http/'):
        url = message.content
        url = url[5:8]
        await channel.send(f"https://http.cat/{url}")

    elif "i love democracy" in message.content:
        await channel.send(file=discord.File('assets/democracy.gif'))

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
