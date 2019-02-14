import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

prefix = ("J")

client = Bot(prefix)

@client.command()
async def website():
   '''Server Website'''
   await client.say("http://www.jellonation.ga")

@client.command()
async def donate():
   '''Server Donations'''
   await client.say("Donations Are Disabled!")


client.run("NDY5MjYzMjQwMDAyNzk3NTkw.D0ZmSg.oLpee2XRENyijvL0ZV4pTdP-E4o")
