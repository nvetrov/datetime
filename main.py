# https://github.com/nvetrov/datetime
# Todo: Mr. Y was born on March 23, 1900 and died on March 18, 1980.  How many seconda did he leave?
import datetime
import time

"""
Мы изучим следующие классы модуля:

datetime.date
datetime.timedelta
datetime.datetime
"""

cur_data = datetime.date(2019, 11, 29)
print(cur_data)
print('----------')
print(cur_data.year)
print(cur_data.month)
print(cur_data.day)
print(cur_data)
print('----------')
print(cur_data.__doc__)
print(f'Today:{datetime.date.today()}')
a = datetime.datetime.today().strftime("%Y%m%d")
print(f'Текущию дату в строку: {a}')
today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d-%H.%M.%S"))
print(time.ctime(4173.571))
print(time.ctime(29215))

a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(a)  # '2017-04-05-00.11.20'

born = datetime.datetime(1900, 3, 23)
died = datetime.datetime(1980, 3, 18)
delta = died - born
print(delta.total_seconds())

