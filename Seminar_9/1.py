"""
📌Создайте функцию-замыкание, которая запрашивает два целых числа: от 1 до 100 для загадывания,
 от 1 до 10 для количества попыток 📌Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
import random


def zam():
    a = random.randint(1, 100)
    b = random.randint(1, 10)
    def inner():
        nonlocal a, b
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

    return inner

prim = zam()
prim()