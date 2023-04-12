"""2. Модель logging"""

# import logging
# logging.info('Немного информации')
# logging.error('Поймали ошибку')


"""Базовые регистраторы.
"""
#
# import logging
# logging.basicConfig(level=logging.NOTSET)
# logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
# logging.info('Немного информации о работе кода')
# logging.warning('Внимание! Надвигается буря!')
# logging.error('Поймали ошибку. Дальше только неизвестность')
# logging.critical('На этом всё')

"""Необходимо использовать функцию уровня модуля
logging.getLogger(name) для получения регистраторов."""
# import logging
#
#
# logging.basicConfig(level=logging.NOTSET)
# logger = logging.getLogger(__name__)
# logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
# logger.info('Немного информации о работе кода')
# logger.warning('Внимание! Надвигается буря!')
# logger.error('Поймали ошибку. Дальше только неизвестность')
# logger.critical('На этом всё')


