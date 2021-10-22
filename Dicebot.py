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


client.run('NzY0MjI4NzU1NDQ3MDg3MTQ0.X4DNfQ.LZ84CynqYkuJYhnMk5Z47DpNW20')
