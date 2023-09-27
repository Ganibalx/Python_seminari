"""
📌Объедините функции из прошлых задач.
📌Функцию угадайку задекорируйте: декораторами для сохранения параметров,
декоратором контроля значений и декоратором для многократного запуска.
📌Выберите верный порядок декораторов.
"""
import json
import os
import random as rnd
from functools import wraps


def save_par(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + '.json'
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8')as f:
                data = json.load(f)
        else:
            data = dict()
        result = func(*args, **kwargs)
        data[result.__repr__()] = {'args': args, 'kwargs': kwargs}
        with open(file_name, 'w', encoding='utf-8')as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return result
    return wrapper


def outer(count):
    def decor(func):
        res = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res
        return wrapper
    return decor


def check_n(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f'Введенное тобой число {a} вне доступного диапазона!')
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print(f'Введенное число {b} вне диапозона!')
            b = rnd.randint(1, 10)
        return func(a, b)
    return wrapper

@save_par
@outer(2)
@check_n
def quess_number(a, b):
    while b:
        print(f'угадай с {b} попыток')
        quess = int(input('Введите число: '))
        if quess < a:
            print('больше')
        elif quess > a:
            print('меньше')
        else:
            print(f'ты угадал c {b} попытки!')
            return f'ты угадал c {b} попытки!'
        b -= 1
    print('У тебя закончились попытки')
    return f'ты не угадал'

quess_number(50, 5)