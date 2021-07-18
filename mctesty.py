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

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= ".", intents=intents)
client.remove_command("help")

##           await message.delete() dodać i asyncio.wait zeby na przyklad po czasie usuwalo

@client.event
async def on_ready():
    print('Pomyślnie zalogowano jako {0.user}'.format(client))

@client.command()
async def x(ctx, arg):
    r = requests.get('https://api.mcsrvstat.us/2/hypixel.net')
    json_data = r.json()

    description = json_data["hostname"]
    online = str(json_data["online"])
    playerCount = str(json_data["ip"])

    embed = discord.Embed(
        title=arg + " Server Info",
        description='Description: ' + description + '\nOnline: ' + online + '\nPlayers: ' + playerCount,
        color=discord.Color.dark_green()
    )
    ##embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

    await ctx.send(embed=embed)



client.run("ODQ4ODAxNjIyODYzMjQ5NDM5.YLR6HA.uis_BEBA_Vlr01-QJJdA1sPuU5U")
