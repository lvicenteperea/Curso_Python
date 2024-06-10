print("************************************************************")
print("Uso de DateTime")
print("************************************************************")

from datetime import datetime

now = datetime.now()

def print_date(date = datetime.now()):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.timestamp())

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime( 2023, 1, 1)
print(year_2023)

print_date(now)
print("")
print_date()

print("************************************************************")
print("Uso de Time")
print("************************************************************")
from datetime import time

current_time = time(12,6,11)

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("************************************************************")
print("Uso de Date")
print("************************************************************")
from datetime import date

current_date = date(2024,8,11)
print(current_date)
print(current_date.month)


print("************************************************************")
print("Operaciones con fechas")
print("************************************************************")
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# curiosamente no se puede aplicar year_2023.time() pero si imprimir....
#diff = year_2023.time() - current_time
#print(diff)
print(year_2023.time())
from datetime import timedelta

init_time_delta = timedelta(200, 100, 100, weeks=10)
end_time_delta = timedelta(300, 100, 100, weeks=14)
print(init_time_delta, end_time_delta)
print(end_time_delta - init_time_delta)

