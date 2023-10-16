"""
📌Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌Например отлавливаем ошибку деления на ноль.
"""
import logging
format = '{asctime:<10} - {levelname:<10} - {msg}'
logging.basicConfig(filename='project.log.', style='{', filemode='w', encoding='utf-8', level=logging.NOTSET, format=format)
logger = logging.getLogger(__name__)

def func(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        logger.error(msg=e)


func(100, 0)