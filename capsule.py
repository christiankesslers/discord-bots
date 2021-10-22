import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_remove(member):
    print(f'{member} opuszcza pokład.')


@client.event
async def on_message(message):
    global server
    if message.content.startswith('.bye'):
        print('ok')
        channel = message.channel
        typek = message.author
        ksywka = message.author.nick
        imie = typek.name

        ident= typek.id
        print(typek, ksywka, ident)



        if ksywka != None:
            await channel.send(f'{ksywka} opuszcza pokład.')
        else:
            await channel.send(f'{imie} opuszcza pokład.')
        await typek.kick()








client.run('NzY0NDk0NDMxNjkxOTk3MjI2.X4HE7A.o3-4P2tVOQJavKLQE719TBHiQjc')
