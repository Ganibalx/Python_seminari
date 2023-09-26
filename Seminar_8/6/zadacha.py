"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import pickle
import json

def read_pickle(path):
    with open(path, 'rb') as pickle_f:
        data = pickle.load(pickle_f)
    return data


def create_csv(data_csv):
    csv_headers = list(data_csv.keys())
    csv_table = list(data_csv.values())
    csv_table = list(zip(*csv_table))
    with open('example.csv', 'w', encoding='utf-8')as file:
        csv_writer = csv.writer(file, dialect='excel', delimiter=' ')
        csv_writer.writerow(csv_headers)
        csv_writer.writerows(csv_table)

data = read_pickle('../5/new_db.pickle')

create_csv(data)
