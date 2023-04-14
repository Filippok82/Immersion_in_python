"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату"""
import logging
from datetime import datetime
from calendar import monthrange

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR, filename='task_04.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)

MONTH = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя','дек')
DAY = ("пон", "вто", "сре", "чет", "пят", "суб","вос")


def data_text(text: str) -> datetime:
    try:
        count, day, month = text.split()
    except ValueError as e:
        logger.error(f'Ошибка введения даты')
        return None
    count = int(count[:-2])
    day = DAY.index(day[:3])
    month = MONTH.index(month[:3]) + 1
    year = datetime.now().year
    count_days = monthrange(year, month)[1]
    # print(count_days)
    count_week = 0
    for d in range(1, count_days+1):
        date = datetime(day= d, month= month, year= year)
        if date.weekday() == day:
            # print(date)
            count_week += 1
            if count == count_week:
                return date

print(data_text('3-я среда мая'))