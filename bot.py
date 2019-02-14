import discord
import asyncio
from discord.ext import commands

prefix = ("J")

client = Bot(prefix)

@client.command()
async def test():
   await client.say("success")


client.run("NDY5MjYzMjQwMDAyNzk3NTkw.D0ZmSg.oLpee2XRENyijvL0ZV4pTdP-E4o")
