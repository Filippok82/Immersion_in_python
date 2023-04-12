"""➢ Формат сохранения события с фигурными скобками
"""

import logging
from loggingn_other import log_all
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
'в строке {lineno:03d} функция "{funcName}()" ' \
'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
