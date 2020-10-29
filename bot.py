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
    x = random.randint(0, 2)
    status = getstatus()
    activity = discord.Activity(type=gettype(x), name=getname(x))
    await client.change_presence(status=status, activity=activity)


@client.event
async def on_message(message):
    # get the channel of the bot and exit the event if the message was from the bot
    if message.content.startswith('.'):
        sentmsg = str(message.content.lower())[1:]
        channel = client.get_channel(message.channel.id)
        if message.author == client.user:
            return
        print(message.content)
        if sentmsg.startswith("help"):
            await channel.send('"." + "help doge latency cringe hey twss noice http/cat ild toyst \'am i ugly\' joke ping meme"')

        elif sentmsg.startswith("doge"):
            api_url = "http://shibe.online/api/shibes?count=1"
            response = await fetch_data(api_url)
            embed = discord.Embed(
                title=f"doge for {message.author}",
            )
            embed.set_image(url=f"{response[0]}")
            await channel.send(embed=embed)

        elif sentmsg.startswith("latency"):
            lat = await channel.send("checking...")
            latutc = sf2utcms(lat.id)
            msutc = sf2utcms(message.id)
            await channel.send(f"Latency: {latutc-msutc} ms.")
        elif sentmsg.startswith("cringe"):
            # open the bleach.txt file
            await channel.send(f"{get_bleach('bleach.txt')}")

        elif sentmsg.startswith("hey"):
            listhey = [f"Hey {message.author.mention}", f"What's up {message.author.mention}",
                       f"Whomst has summoned the almighty one\nOh it's you {message.author.mention}"]
            await channel.send(f"{listhey[random.randint(0, len(listhey)-1)]}")
        elif sentmsg.startswith("twss"):
            await channel.send(file=discord.File(f'assets/twss{random.randint(0, 1)}.gif'))

        elif sentmsg.startswith("noice"):
            await channel.send(file=discord.File('assets/tenor.gif'))

        elif sentmsg.startswith("http/"):
            url = sentmsg
            url = url[5:8]
            await channel.send(f"https://http.cat/{url}")

        elif sentmsg.startswith("ild"):
            await channel.send(file=discord.File('assets/democracy.gif'))

        elif sentmsg.startswith("toyst"):
            await channel.send("https://media1.tenor.com/images/2fb6b048517ffc9492dfea5766d3835d/tenor.gif")

        elif sentmsg.startswith("am i ugly"):
            replies = [
                "It runs in your fam bitch",
                "Nah man you beautiful", "Yes.", "What if I told no"
            ]
            await channel.send(f'{random.choice(replies)}')

        elif sentmsg.startswith("joke"):
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
        elif sentmsg.startswith("ping"):
            os.system("ping google.com -c 1 1>ping")
            with open('ping') as pingfile:
                for line in nonblank_lines(pingfile):
                    await channel.send(f'{line}')
        elif sentmsg.startswith("meme"):
            subreds = ["memes", "dankmemes", "programmerhumor", "boneappletea", "funny",
                       "interestingasfuck", "murderedbywords"]
            n = subreds[random.randint(0, len(subreds)-1)]
            # get the meme
            meme = await fetch_data(f"https://meme-api.herokuapp.com/gimme/{n}")
            embed = discord.Embed(
                title=f'{str(meme["title"])}',
            )
            embed.url = str(meme["postLink"])
            embed.set_image(url=f'{str(meme["url"])}')
            embed.set_author(
                name=f'u/{str(meme["author"])} on {str(meme["subreddit"])}')
            await channel.send(embed=embed)

if __name__ == '__main__':
    sys.stdout.flush()
    client.run(TOKEN)
