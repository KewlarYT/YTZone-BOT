from typing import Awaitable
from discord import activity, user
from discord.ext.commands import Bot
import time
import random
import asyncio 
import discord 
from discord.utils import get 
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= "?", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.event
async def on_member_join(member):
    kanal = discord.utils.get(member.guild.channels, id=852964674440790046)
    rola = discord.utils.get(member.guild.roles, id=852039947635523614)
    await member.add_roles(rola)
    await kanal.send(f"{member.mention} cześć!!!")

@client.event
async def on_member_remove(member):
    kanal = discord.utils.get(member.guild.channels, id=852964674440790046)
    await kanal.send(f"{member.name} żegnaj!!!")

@client.event
async def on_message(message):
    slowa = ['jd', 'jr']
    for i in slowa:
        if i == message.content:
            rola = discord.utils.get(message.author.guild.roles, id=852039947635523614)
            await message.author.remove_roles(rola)
            await message.channel.send("nie pisz tak")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embedVar = discord.Embed(title="Witaj!", description=":wrench: Mój prefix to: ``.``\n:tools: Najważniejsze informacje dotyczące bota znajdziesz pod: ``.pomoc``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('.pomoc'):
        embedVar = discord.Embed(title="Pomoc | Najważniejsze informacje", description=":clipboard: Liste wszystkich komend znajdziesz pod: ``.komendy``\n:video_game: Opis bota YT Zone znajdziesz pod: ``.opis``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help ", url="https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A", description="Commands", color=0xeb1e1e)
    embed.add_field(name="help", value="pokazuje okienko", inline=False)
    embed.add_field(name="test", value="test", inline=False)
    embed.add_field(name="test1", value="test1", inline=False)
    await ctx.send(embed=embed, delete_after = 10)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Zbanowano {member.mention} za {reason}", delete_after=10)

@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.kick(reason=reason)
    await ctx.channel.send(f"Wyrzucono <@{member.id}> za {reason}", delete_after=10)

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
