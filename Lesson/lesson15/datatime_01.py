"""3. Модуль datetime
Создаём дату и время
"""
#
# from datetime import time, date, datetime
#
# d = date(year=2007, month=6, day=15)
# t = time(hour=2, minute=14, second=0, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
#               second=0, microsecond=24)
# print(f'{d = }\t-\t{d}')
# print(f'{t = }\t-\t{t}')
# print(f'{dt = }\t-\t{dt}')
#
#

"""Разница времени"""

# from datetime import timedelta
#
# delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5,
# milliseconds=6, microseconds=7)
# print(f'{delta = }\t-\t{delta}')

"""Delta может быть отрицательной"""
# from datetime import timedelta
#
# delta = timedelta(weeks=53, days=500, hours=73, minutes=101,
#                   seconds=303, milliseconds=67890,
#                   microseconds=1234567)
# neg_delta = timedelta(days=-3, minutes=-42)
# print(f'{delta = }\t-\t{delta}')
# print(f'{neg_delta = }\t-\t{neg_delta}')


"""Математика с датами
"""

# from datetime import datetime, timedelta
#
# date_1 = datetime(2012, 12, 21)
# date_2 = datetime(2017, 8, 19)
# delta = date_2 - date_1
# print(f'{delta = }\t-\t{delta}')
# birthday = datetime(1503, 12, 14)
# dlt = timedelta(days=365.25 * 33)
# new_date = birthday + dlt
# print(f'{new_date = }\t-\t{new_date}')


"""Доступ к свойствам
Каждый из объектов позволяет прочитать хранимые свойства обратившись к ним
по имени через точечную нотацию."""

# from datetime import time, date, datetime, timedelta
#
# d = date(year=2007, month=6, day=15)
# t = time(hour=2, minute=14, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
#               microsecond=24)
# delta = timedelta(weeks=53, hours=73, minutes=101,
#                   seconds=303, milliseconds=60)
# print(f'{d.month}')
# print(f'{t.second}')
# print(f'{dt.hour}')
# print(f'{delta.days}')

# __________________________________________________________


# from datetime import time, date, datetime, timedelta
#
# t = time(hour=2, minute=14, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
#               microsecond=24)
# new_dt = dt.replace(year=2012)
# one_more_hour = t.replace(t.hour + 1)
# print(f'{new_dt}\n{one_more_hour}')

"""Другие методы работы с датой и временем"""

# from datetime import datetime
#
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
#               microsecond=24)
# print(dt)
# print(dt.timestamp())
# print(dt.isoformat())
# print(dt.weekday())
# print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S.Это %W неделя и %j день года.'))


"""несколько обратных методов, позволяющих создать объекты datetime."""

from datetime import datetime

date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время02 :14:00. Это 24 неделя и 166 день года.'

original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date)
print(timestamp_date)
print(iso_date)
print(text_date)
