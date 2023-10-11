"""
📌Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7)
сохраняя информацию в JSON файл.
📌Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует
 множество пользователей.
"""
import json
import os


class User:
    def __init__(self, name, the_id, level):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self._id = the_id
        if not isinstance(the_id, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть числом от 1 до 7')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self._id = }, {self.level}'

    def __eq__(self, other):
        if isinstance(other, User):
            return all((self.name == other.name, self._id == other._id))


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}
    return data

def worker(id, name, level):
    try:
        new_user = User(name, int(id), int(level))
        return new_user
    except ValueError as e:
        print(e)

def save_json(path, user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)

def add_user(user_db, new_user):
    if str(new_user._id) not in user_db.keys():
        user_db[new_user._id] = {'name': new_user.name, 'level': new_user.level}
    return user_db


if __name__ == '__main__':
    path = 'my_user.json'
    user_db = load_json(path)
    new_user = worker(0.5, 'Антон', 2)
    user_db = add_user(user_db, new_user)
    save_json(path, user_db)


