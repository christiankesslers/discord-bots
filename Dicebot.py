import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def dice(ctx, rn=6):
    await ctx.send(f'Score: {random.randint(1,rn)}')


client.run('wxLQD3PsuW3CmtyIdFv_LBpHc2xpGmF2q5zyAjBHdvyqgYrPnESRvamfkPpdffNOyYyM')