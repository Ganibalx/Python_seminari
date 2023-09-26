"""Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
📌Имена пишите с большой буквы.
📌Каждую пару сохраняйте с новой строки.
"""
import json

def createjson():
    with open('file3.txt', 'r', encoding='utf-8') as data:
        my_dict = dict()
        for _ in data:
            l = data.readline()
            if len(l) > 1:
                a, b = l[:-1].split()
                my_dict[a.title()] = b

    with open('my.json', 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, indent=4, ensure_ascii=False)

createjson()