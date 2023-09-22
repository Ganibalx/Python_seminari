'''✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

 Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

import os
import pathlib
import random

SLOVAR = 'абвгдежзиклмнопрстуфхцчшщьыъэюя'

def file_creator(*, dir, ras, min_len=6, max_len=30, min_data=256, max_data=4096, file_count=42):
    for _ in range(file_count):
        name = ''
        for _ in range(random.randint(min_len, max_len)):
            name += random.choice(SLOVAR)
        if not os.path.exists(dir):
            pathlib.Path(dir).mkdir(parents=True)
        if os.path.exists(file:=pathlib.Path.cwd()/dir/f'{name}.{ras}'):
            flag = True
            i = 0
            while flag:
                if os.path.exists(file:=pathlib.Path.cwd() / dir / f'{name}{i}.{ras}'):
                   i += 1
                else:
                    flag = False
        with open(file, 'wb')as data:
            data.write(os.getrandom(random.randint(min_data, max_data)))


def creator_v2(*, dir='file', **kwargs):
    for i in kwargs:
        file_creator(ras=i, min_len=3, max_len=6, file_count=kwargs[i], dir=dir)


if __name__ == '__main__':
    creator_v2(dir='file', avi=2, jpg=3, drf=4, xz=2)

