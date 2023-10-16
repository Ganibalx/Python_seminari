"""
📌На семинаре про декораторы был создан логирующий декоратор.
Он сохранял аргументы функции и результат её работы в файл.
📌Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""
import logging


def dec(func):
    format = '{msg}'
    logging.basicConfig(filename='my.log.', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET,
                        format=format)
    logger = logging.getLogger(__name__)

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