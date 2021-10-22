from datetime import date, timedelta, datetime
import decimal


today = date.today()
print("Today's date:", today)

#data
EndDate = date.today() + timedelta(days=10)
print(EndDate)

Stardate_zero = date(2397, 3, 30)
delta= Stardate_zero - date.today()
print(delta.days)




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
print(h)
print(m)
print(s)
print('myt ', myt)
print('devision ', devision)
print('score', sc)
st = input('>')
stepone = str(st)
steptwoa, steptwob = stepone.split('.')
print(steptwoa)
print(steptwob)
hour = str((int(steptwob)/100000) * 24)
print(hour)
hor, min = hour.split('.')
print(hor, ' ', min)
minute = float('0'+'.'+min)*60
print(minute)
minutka, sec = str(minute).split('.')
sekunda = int(float('0'+'.'+sec)*60)
print(minutka)
print(sekunda)

#ADATA
#st -> ed:
roznica = int(steptwoa) - 74243
yeart,montht,dayt = str(Stardate_zero + timedelta(days=roznica)).split('-')




print(datetime(int(yeart),int(montht),int(dayt),int(hor),int(minutka),int(sekunda)))
