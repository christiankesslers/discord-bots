import discord
import pytz
from discord.ext import commands
from datetime import date, timedelta, datetime

client = commands.Bot(command_prefix = '.')

#data, dane, obliczenia
today = date.today()
print(today)
stardate_zero = date(2397, 3, 30)
days_apart = 137501
my_star_date = date.today() + timedelta(days=days_apart)
print(my_star_date)
delta = my_star_date - stardate_zero
days_to_add = delta.days
print(delta.days)
date_to_print = 74243 + days_to_add
print(date_to_print)

#godzina
h =datetime.now().hour
m =datetime.now().minute
s =datetime.now().second

maxt = 24*3600
myt = s + 60*m + 3600*h
devision = myt/maxt
sc = "%.5f" % round(devision, 5)

#końcowy wynik:
to_print = float(date_to_print) + float(sc)
print(to_print)
#koniec

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'Witamy na pokładzie {member}!')

@client.event
async def on_member_remove(member):
    print(f'{member} opuszcza pokład.')

@client.command()
async def helpme(message):

    channel = message.channel
    typek = message.author
    ksywka = message.author.nick

    imie = typek.name
    watar = typek.avatar
    dyck = typek.discriminator
    if ksywka != None:
        await channel.send(f'Hello to Argo, {ksywka}')
    else:
       await channel.send(f'Hello to Argo, {imie}')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def dater(ctx, yr=None, mn=None, dy=None, hr=None, mi=None, se=None):
    global timedelta
    global delta
    global date
    global datetime

    if yr==None and mn==None and dy==None and hr==None and mi==None and se==None:

        #data, dane, obliczenia
        today = date.today()
        stardate_zero = date(2397, 3, 30)
        days_apart = 137501
        my_star_date = date.today() + timedelta(days=days_apart)
        print(my_star_date)
        delta = my_star_date - stardate_zero
        days_to_add = delta.days
        print(delta.days)
        date_to_print = 74243 + days_to_add
        print(date_to_print)

        #godzina
        h =datetime.now().hour
        m =datetime.now().minute
        s =datetime.now().second

        maxt = 24*3600
        myt = s + 60*m + 3600*h
        devision = myt/maxt
        sc = "%.5f" % round(devision, 5)

        to_print = "%.5f" % round(float(date_to_print) + float(sc),5)
        print(to_print)

        await ctx.send(f'Date: {today}, {h}:{m}:{s}')
        await ctx.send(f'Stardate: {to_print}')
        await ctx.send(f'Earthdate: {my_star_date}, {h}:{m}:{s}')

    elif yr!=None and mn!=None and int(mn)>0 and int(mn)<13 and dy!=None and int(dy)>0 and int(dy)<32 and hr!=None and int(hr)<25 and mi!=None and int(mi)<61 and se!=None and int(se)<61:
        print('ok')
        #data, dane, obliczenia
        yr=int(yr)
        mn=int(mn)
        dy=int(dy)
        mi=int(mi)
        hr=int(hr)
        se=int(se)
        today = date(yr,mn,dy)
        stardate_zero = date(2397, 3, 30)
        days_apart = 137501
        my_star_date = date.today() + timedelta(days=days_apart)
        print(my_star_date)
        delta = my_star_date - stardate_zero
        days_to_add = delta.days
        print(delta.days)
        date_to_print = 74243 + days_to_add
        print(date_to_print)

        #godzina

        maxt = 24*3600
        myt = se + 60*mi + 3600*hr
        devision = myt/maxt
        sc = "%.5f" % round(devision, 5)

        to_print = "%.5f" % round(float(date_to_print) + float(sc),5)
        print(to_print)

        await ctx.send(f'Date: {today}, {hr}:{mi}:{se}')
        await ctx.send(f'Stardate: {to_print}')
        await ctx.send(f'Earthdate: {my_star_date}, {hr}:{mi}:{se}')

    else:
        await ctx.send('Beep! Boop! Wprowadzone dane są błędne. Wyślij ".helpargo", by uzyskać więcej informacji.')


@client.command()
#przyjmuje stardate i daje date oraz earthdate
async def edate(ctx, dt=None):
    global stardate_zero
    global timedelta
    global delta
    global date
    global datetime

    stepone = str(dt)
    steptwoa, steptwob = stepone.split('.')
    day = int(steptwoa)

#liczba sekund jakie upłynęły danego dnia:
    hour = (int(steptwob)/100000) * 24
    hor, min = str(hour).split('.')
    print(hor, ' ', min)
    minute = float('0'+'.'+min)*60
    print(minute)
    minutka, sec = (str(minute)).split('.')
    sekunda = int(round(float('0'+'.'+sec)*60))
    if sekunda==60:
        sekunda=0
        minutka=0
        hor= int(hor)+1
    else:
        print('ok')


    #godzina to będzie hor:minutka:sekunda


    roznica = int(steptwoa) - 74243
    yeart,montht,dayt = str(stardate_zero + timedelta(days=roznica)).split('-')
    earthdate = datetime(int(yeart),int(montht),int(dayt),int(hor),int(minutka),int(sekunda))

    print(earthdate)

    now_date = earthdate + timedelta(days=-137501)
    await ctx.send(f'Stardate: {dt}')
    await ctx.send(f'Date: {now_date}')
    await ctx.send(f'Earthdate: {earthdate}')


@client.command()
#przyjmuje earthdate i daje st date oraz date
async def sdate(ctx, dt=None):
    await ctx.send(f'Hello!')

@client.command()
async def helpargo(ctx):
    await ctx.send('Help')
'''
@client.command()
async def helpme(ctx):


    print('ok')'''



@client.command()
async def alert(ctx, color, reason=None):
    channels = [764225303571595294, 764225257325723668, 764225650693242922, 764226064389373972,726405903678701618,726405984712523857,726406111841878018,726406154854334545,726406211553067028,726405847491805255,726405674015129620,
                765210654796939315,764227951574122566,741398793806938162,726406796654280746,726406608103669830,726406558900027462,726406311176044544,726406264015290441,726405571489693719,726405304971034625,726405138121490494,726404771673538601,726404717139460137,726404666497302542,726404610805202984,
                726404496179068989,726404356370464830,726404178775113771,726402933733720115]

    if color == 'red':
        print('red alert')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send('''```css\n
[RED ALERT!!! RED ALERT!!! RED ALERT!!!]```''')
            if reason!=None:
                await channel.send(f'''```css\n
[{reason}]```''')

    if color == 'yellow':
        print('yellow')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send('''```fix\n
[YELLOW ALERT! YELLOW ALERT! YELLOW ALERT!]```''')
            if reason!=None:
                await channel.send(f'''```fix\n
[{reason}]```''')



    if color == 'blue':
        print('blue')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send('''```ini\n
[BLUE ALERT! BLUE ALERT! BLUE ALERT!]```''')
            if reason!=None:
                await channel.send(f'''```ini\n
[{reason}]```''')


    if color == 'birthday':
        print('birthday')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send('''```diff\n
+ BIRTHDAY ALERT! BIRTHDAY ALERT! BIRTHDAY ALERT! +```''')
            if reason!=None:
                await channel.send(f'''```diff\n
+{reason}+```''')


    if color =='reed':
        print('reed')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send('''```bash\n
"REED ALERT! <3 REED ALERT! <3 REED ALERT! <3"
```''')
            if reason!=None:
                await channel.send(f'''```bash\n
"{reason}"```''')

    if color =='white':
        print('white')
        for ides in channels:
            channel = client.get_channel(ides)
            await channel.send("""```bash\n
IMPORTANT! IMPORTANT! IMPORTANT!```""")
            if reason!=None:
                await channel.send(f"""```bash\n
TO ALL CREW: {reason}```""")

@client.command()
async def alertoff(ctx, amount=1, search=100):

    channels = [764225303571595294, 764225257325723668, 764225650693242922, 764226064389373972,726405903678701618,726405984712523857,726406111841878018,726406154854334545,726406211553067028,726405847491805255,726405674015129620,
                765210654796939315,764227951574122566,741398793806938162,726406796654280746,726406608103669830,726406558900027462,726406311176044544,726406264015290441,726405571489693719,726405304971034625,726405138121490494,726404771673538601,726404717139460137,726404666497302542,726404610805202984,
                726404496179068989,726404356370464830,726404178775113771]
    messages = []
    for ides in channels:
        channel = client.get_channel(ides)
        licznik = 0
        async for message in channel.history(limit =search):
            if (licznik < amount) and (message.author.name == "Argo") and message.content.startswith("""```"""):
                messages.append(message)
                licznik +=1

        await channel.delete_messages(messages)




client.run('NzMwMzk1MzAyODQ2MDA1Mjg4.XwW3og.GyMexvx7UGmDL4RqcHI2FOXMIkc')
