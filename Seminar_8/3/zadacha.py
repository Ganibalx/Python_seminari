"""Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
📌После каждого ввода добавляйте новую информацию в CSV файл.
📌Пользователи группируются по уровню доступа.
📌Идентификатор пользователя выступает ключём для имени.
📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
📌При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import csv
import json
import os.path

DB = 'my.json'
CSV_FILE = 'my.csv'

def get_user_id(db):
    users_id = set()
    for user in db.values():
        users_id.add(user[1])
    return users_id


def new_user():
    user_db = readjson()
    while True:
        name = input_name()
        if not name:
            break
        id_ = input_id(user_db)
        lvl = input_lvl()

        if lvl in user_db:
            user_db[lvl].append({id_: name})
        else:
            user_db[lvl] = [{id_: name}]
        with (open(DB, 'w', encoding='utf-8') as file,
              open(CSV_FILE, 'w', encoding='utf-8') as file_csv):
            json.dump(user_db, file, indent=4, ensure_ascii=False)
            result = []
            for lvl, users in user_db.items():
                for user in users:
                    for u_id, name in user.items():
                        result.append((name, u_id, lvl))
            csv_writer_ = csv.writer(file_csv, dialect='excel')
            csv_writer_.writerows(result)

def input_name():
    return input('Введите имя: ')


def input_id(dict_users):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)
    while True:
        u_id = input('Введите ID: ')
        if u_id not in list_id:
            return u_id


def input_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 0 < int(lvl) < 8:
            return lvl


def readjson():
    if os.path.exists(DB):
        with open(DB, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}
    return data


new_user()