from typing import Awaitable
from discord import activity, user
from discord.ext.commands import Bot, bot
import time
import random
import asyncio 
import discord 
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get 
import requests
import datetime

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= ".", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.event
async def x():
    while True:
        await client.wait_until_ready()

        r = requests.get('https://api.mcsrvstat.us/2/134.255.252.95:2042')
        json_data = r.json()
        channel = client.get_channel(866350714551926784)
        print(channel)
        try:
            ip = json_data["ip"]
            online = str(json_data["online"])
            playerCount = str(json_data["players"]["online"])
            maxCount = str(json_data["players"]["max"])

        except KeyError:
            print("Serwer YT Zone Minecraft jest wyłączony")
    
        if online == "True":
            embed = discord.Embed(
            title="Serwer Online!",
                description='IP Serwera: ' + ip + '\nIlość graczy: ' + playerCount + "/" + maxCount + "\nWersja: 1.14",
                color=discord.Color.green()
            )

            embed.timestamp = datetime.datetime.utcnow()
            embed.set_thumbnail(url="https://i.imgur.com/9zmVAkY.png?fit=500%2C500&ssl=1")

            await channel.send(embed=embed, delete_after=60)
        else:
            embed = discord.Embed(
                title="Serwer Offline!",
                description='Serwer Youtubers Zone Minecraft jest aktualnie wyłączony. Jeśli nie jest to planowana przerwa techniczna, prosimy o powiadomienie administracji serwera.',
                color=discord.Color.dark_red()
            )

            embed.timestamp = datetime.datetime.utcnow()
            embed.set_thumbnail(url="https://i.imgur.com/9zmVAkY.png?fit=500%2C500&ssl=1")

            await channel.send(embed=embed, delete_after=60)

        await asyncio.sleep(60)


client = discord.Client()

client.loop.create_task(x())
client.run("NzY0MzQzMTgwMDkwMTQ2ODU2.X4E4Dg.OjpX0Sl3m8iwOCDf03IxXQeGLJI")
