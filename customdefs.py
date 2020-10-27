import discord
import aiohttp
import random


async def fetch_data(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            return await r.json()


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def sf2utcms(sf):
    return ((sf >> 22) + 1288834974657)


def getname(x):
    dic = {}
    dic[0] = ["you", "your girlfriend", "skynet", "TV", "my fish"]
    dic[1] = ["football", "with my life", "with skynet", "with myself :("]
    dic[2] = ["After Hours", "Kiss Land", "Daft Punk - TRON: Legacy",
              "Beauty Behind the Madness", "Trilogy", "My Dear Melancholy"]
    return dic[x][random.randint(0, len(dic[x])-1)]


def getstatus():
    dic = {}
    dic[0] = discord.Status.do_not_disturb
    dic[1] = discord.Status.idle
    dic[2] = discord.Status.online
    return dic[random.randint(0, len(dic)-1)]


def gettype(x):
    dic = {}
    dic[0] = discord.ActivityType.watching
    dic[1] = discord.ActivityType.playing
    dic[2] = discord.ActivityType.listening
    return dic[x]
