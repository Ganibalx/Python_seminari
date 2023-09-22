# Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.
import random as rnd


def my_gen_name(min, max):
    sogls = 'бвгджзйклмнпрстфхцчшщьъ'
    glas = 'aеиоуыэюя'
    while True:
        result = [0]*rnd.randint(min, max)
        for i in range(len(result)):
            result[i] = rnd.choice(sogls) if i % 2 == 0 else rnd.choice(glas)
        yield ''.join(result).title()


def file_write(file, count):
    gen = my_gen_name(4, 7)
    with open(file, 'a', encoding='utf-8') as data:
        for _ in range(count):
            data.write(f'{next(gen)}\n')

file_write('file2.txt', 10)