from datetime import date,datetime,timedelta
agora = datetime.now()
print(agora)

hora = datetime.hour
minuto = datetime.min
dia = datetime.day
mes = datetime.month
ano = datetime.year

print(dia,mes,ano,hora,minuto)

time_one = agora.strftime("%d/%m/%Y, %H:%M:%S")
print("time_one: ",time_one)

string_data = "5 December, 2019"
print("date_string: ", string_data)
date_time = datetime.strptime(string_data,"%d %B, %Y")
print("date_time: ",date_time)

tempo_agora = date(year=2026,month=8,day=9)
novo_ano = date(year=2027,month=1,day=1)

diff = novo_ano - tempo_agora
print("Diferença até o ano novo: ",diff)

ano_1970 = date(year=1970,month=1,day=1)

diff2 = ano_1970 - tempo_agora

print("Diferença entre 1970 e Hoje: ",diff2)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)