import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

prefix = ("?")
client = Bot(prefix)

@client.command()
async def website():
   '''Server Website'''
   await client.say("http://www.jellonation.ga")

@client.command()
async def donate():
   '''Server Donations'''
   await client.say("Donations Are Disabled!")


client.run("YOUR_BOT_TOKEN_GOSE_HERE")
