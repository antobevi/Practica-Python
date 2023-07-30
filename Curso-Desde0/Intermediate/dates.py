from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now() # Si importo toda la libreria de date time seria: datetime.datetime.now()

print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)
print(now.timestamp()) # Tiempo calculado desde 1970, se puede convertir a un formato mas declarativo
print(now.timestamp())

current_time = time() # Si importamos toda la libreria de date time seria: datetime.time()
# Si no le pasamos nada a time por parametro nos trae 0 para cada valor

print(current_time)

current_date = date.today()
current_date = datetime.now()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(current_date.year, current_date.month + 1, current_date.day) # Esta es la forma de hacer operaciones

current_year_2023 = datetime(2023, 6, 1)

print(now)
print(current_year_2023)
print(now - current_year_2023) # Ambos son del tipo datetime
print(current_date - current_year_2023.date()) # Ambos son del tipo date

# Para operar con diferentes fechas usamos el TIMEDELTA
# El timedelta no es para trabajar con fechas, si no que nos permite trabajar con franjas de fechas
# Con timedelta indicamos un espacio de tiempo que dura x dias, x semanas, etc.
start_time_delta = timedelta(200, 100, 1000, weeks=3) # 200 dias, 100 minutos, 1000 milisegundos
# y weeks=3 cuando no sigo el patron
end_time_delta = timedelta(300, 200, 2000, weeks=4)

print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)
# podemos dividir pero no multiplicar