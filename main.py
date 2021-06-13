from typing import Awaitable
from discord import activity, user
from discord.ext.commands import Bot
import time
import random
import asyncio 
import json 
import discord 
from discord.utils import get 
from discord.ext import commands 

client = commands.Bot(command_prefix= ".")
bot = commands.Bot(command_prefix=".")
client.remove_command("help")

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embedVar = discord.Embed(title="Witaj!", description=":wrench: Mój prefix to: ``.``\n:tools: Najważniejsze informacje dotyczące bota znajdziesz pod: ``.pomoc``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('.pomoc'):
        embedVar = discord.Embed(title="Pomoc | Najważniejsze informacje", description=":clipboard: Liste wszystkich komend znajdziesz pod: ``.komendy``\n:video_game: Opis bota YT Zone znajdziesz pod: ``.opis``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

@client.event
async def statusy():
    await client.wait_until_ready()
    statuses = ["🔴 | Youtubers Zone 2.0", "❓ | .pomoc"]
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)


client.loop.create_task(statusy())

client.run("ODQ4ODAxNjIyODYzMjQ5NDM5.YLR6HA.uis_BEBA_Vlr01-QJJdA1sPuU5U")
