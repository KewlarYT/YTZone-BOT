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

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= ".", intents=intents)
client.remove_command("help")

##           await message.delete() dodać i asyncio.wait zeby na przyklad po czasie usuwalo

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.event
async def on_member_join(member):
    kanal = discord.utils.get(member.guild.channels, id=714198844887531621)
    rola = discord.utils.get(member.guild.roles, id=0)
    await member.add_roles(rola)
    embedVar = discord.Embed(title="Witaj " f"{member.name}" "!", description=":clipboard: jakiś tekst: ``.jakiś tekst``\n:video_game: jakiś tekst: ``.jakiś tekst``", color=0xFF0000)
    await kanal.send(embed=embedVar)
    await kanal.send(f"{member.mention}", delete_after=2)

@client.event
async def on_member_remove(member):
    kanal = discord.utils.get(member.guild.channels, id=714198844887531621)
    embedVar = discord.Embed(title="Żegnaj!", description=f":clipboard: **{member.name}** wyszedł z serwera YT | Zone", color=0xFF0000)
    await kanal.send(embed=embedVar)

##!!NIE DZIAŁA!!
##@client.event
##async def on_message(message):
##    slowa = ['jd', 'jr']
##    for i in slowa:
##        if i == message.content:
##            rola = discord.utils.get(message.author.guild.roles, id=852039947635523614)
##            await message.author.remove_roles(rola)
##            await message.channel.send("nie pisz tak")

@client.command()
async def dev(ctx):
    embed=discord.Embed(title="Help ", url="https://www.youtube.com/channel/UC4vtx0j0wcP6s4n7hCTUs7A", description="Commands", color=0xeb1e1e)
    embed.add_field(name="help", value="pokazuje okienko", inline=False)
    embed.add_field(name="test", value="test", inline=False)
    embed.add_field(name="test1", value="test1", inline=False)
    await ctx.send(embed=embed, delete_after = 10)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    kanal = discord.utils.get(member.guild.channels, id=716426907008237568)
    await member.ban(reason=reason)
    await ctx.channel.send(f"Zbanowano {member.mention} za {reason}", delete_after=10)
    embedVar = discord.Embed(title="Użytkownik " f"{member.name}" " został zbanowany!", description=f":clipboard: **Powód:** {reason}", color=0xFF0000)
    await kanal.send(embed=embedVar)
    await ctx.message.delete()

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Odbanowano {user.mention}', delete_after=10)
            await ctx.message.delete()

@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    kanal = discord.utils.get(member.guild.channels, id=716426907008237568)
    await member.kick(reason=reason)
    await ctx.channel.send(f"Wyrzucono <@{member.id}> za {reason}", delete_after=10)
    embedVar = discord.Embed(title="Użytkownik " f"{member.name}" " został wyrzucony!", description=f":clipboard: **Powód:** {reason}", color=0xFF0000)
    await kanal.send(embed=embedVar)
    await ctx.message.delete()

@client.command()
@has_permissions(ban_members=True)
async def aktualizacja(ctx, numer="---", reason="Bez Powodu"):
    member = ctx.message.author
    kanal = discord.utils.get(member.guild.channels, id=696260706890416138)
    await ctx.channel.send(f"Zamieszczenie aktualizacji udane! Treść: {reason}", delete_after=10)
    embedVar = discord.Embed(title=f"Aktualizacja {numer}!", description=f":tools: **Zmiany:** {reason}", color=0xFF0000)
    await kanal.send(embed=embedVar)
    await ctx.message.delete()    

@client.command()
async def status(message):
    embedVar = discord.Embed(title="Status bota YT | Zone", description=":fire: Bot jest online i funkcjonuje poprawnie!", color=0x00FF00)
    await message.channel.send(embed=embedVar)

@client.command()
async def info(message):
        embedVar = discord.Embed(title="Informacje dotyczące bota", description=":clipboard: Liste wszystkich komend znajdziesz pod: ``.komendy``\n:video_game: Opis bota YT Zone znajdziesz pod: ``.opis``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

@client.command()
async def pomoc(message):
        embedVar = discord.Embed(title="Witaj!", description=":wrench: Mój prefix to: ``.``\n:tools: Najważniejsze informacje dotyczące bota znajdziesz pod: ``.info``", color=0xFF0000)
        await message.channel.send(embed=embedVar)

@client.event
async def statusy():
    await client.wait_until_ready()
    statuses = ["🔴 | Youtubers Zone 2.0", "❓ | .pomoc", "🎮 | Wersja 0.1"]
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)



client.loop.create_task(statusy())

client.run("NzY0MzQzMTgwMDkwMTQ2ODU2.X4E4Dg.OjpX0Sl3m8iwOCDf03IxXQeGLJI")
