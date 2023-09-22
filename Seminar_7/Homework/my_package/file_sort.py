"""✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
import os
import pathlib


def file_sort(**kwargs):
    for i in kwargs.keys():
        if not os.path.exists(i):
            pathlib.Path(pathlib.Path.cwd() / 'file' / i).mkdir()
    p = pathlib.Path(pathlib.Path.cwd() / 'file')
    for i in p.iterdir():
        if i.is_file():
            n = i.name.split('.')
            for j, val in kwargs.items():
                if n[1] in val:
                    i.replace(pathlib.Path.cwd() / 'file' / j / i.name)



