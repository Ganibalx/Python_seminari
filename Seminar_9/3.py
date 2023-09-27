"""
📌Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
 который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌Для декорирования напишите функцию, которая может принимать как позиционные,
так и ключевые аргументы. 📌Имя файла должно совпадать с именем декорируемой функции.
"""
import json
import os


def dec(func):
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + '.json'
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8')as f:
                data = json.load(f)
        else:
            data = dict()
        result = func(*args, **kwargs)
        data[result] = {'args': args, 'kwargs': kwargs}
        with open(file_name, 'w', encoding='utf-8')as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return result
    return wrapper

@dec
def func(a, b):
    return a + '_' + b

print(func('Первая', 'Вторая'))
print(func(a='Попытка', b='Два'))
print(func('Третья', b='пфытка'))