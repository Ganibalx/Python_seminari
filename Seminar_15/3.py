"""
📌Доработаем задачу 2.
📌Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
"""

import logging
from functools import wraps


def dec(func):
    format = '{levelname:<5} - {asctime:<20} - {funcName} - {msg}'
    logging.basicConfig(filename='my.log.', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET,
                        format=format)
    logger = logging.getLogger(__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = 'args: ' + ', '.join(args)
        if kwargs:
            str_kwargs = 'kwargs: ' + ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        logger.info(msg=f'{result = }, {str_args}' + f'{", " if args and args else " "}' + f'{str_kwargs}')
        return result
    return wrapper

@dec
def func(a, b):
    return a + '_' + b

print(func('Первая', 'Вторая'))
print(func(a='Попытка', b='Два'))
print(func('Третья', b='пфытка'))