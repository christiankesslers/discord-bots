import discord
import pytz
from discord.ext import commands
from datetime import date, timedelta, datetime

#zrobić, żeby cleaner usuwał wiadomości logbota tylko gdy da mu się komendę .clean/.clear [liczba] log
#chce zrobić, żeby log mógł zapisywać X ostatnich wiadomości danego kanału w osobnym kanale "log"-> funkcja .log [ilość wiadomości do zapisania, here lub nic],
#.log all -> zapisze wszystkie wiadomości z danego kanału
#.log personal -> zapisze tylko nasze wiadomości
#.log coś here -zapisze all, personal, lub ileś wiadomości na kanale, gdzie została użyta
client = commands.Bot(command_prefix = '.')
@client.command()
async def log(ctx, amount=1, where=None):
    print(1)

@client.event
async def on_ready():
    print('Bot is ready')

client.run('NzY3MTExOTQ4NDM3MjkxMDg5.X4tKrA.cZqD_H4bfM5F2xHl37_WakRqzLY')
