"""
📌Дорабатываем задачу 1.
📌Превратите внешнюю функцию в декоратор.
📌Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
📌Если не входят, вызывать функцию со случайными числами из диапазонов.
"""
import random as rnd

def decor(func):
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f'Введенное тобой число {a} вне доступного диапазона!')
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print(f'Введенное число {b} вне диапозона!')
            b = rnd.randint(1, 10)
        func(a, b)
    return wrapper

@decor
def inner(a, b):
    while b:
        print(f'угадай с {b} попыток')
        quess = int(input('Введите число: '))
        if quess < a:
            print('больше')
        elif quess > a:
            print('меньше')
        else:
            print(f'ты угадал c {b} попытки!')
            return
        b -= 1

inner(150, 6)
