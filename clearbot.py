import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def clean(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

client.run('NzY0NDgzNjIzMzgxMzY4OTAz.X4G62w.I_WabUdM6E4jBPgHAa_VB-In7Tg')


