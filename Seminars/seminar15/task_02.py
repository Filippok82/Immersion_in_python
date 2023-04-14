"""На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""

import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='task02.log',
                    encoding='utf-8', format=FORMAT, style="{")
logger = logging.getLogger(__name__)


def deco_file(func):
    data = []

    def wrapper(*args, **kwargs):
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        # print(new_data)
        logger.info(new_data)
        return result

    return wrapper


@deco_file
def call(*args, **kwargs):
    pass


call(12, 24, 56, ax=12, b=45)