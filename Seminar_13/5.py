"""
📌Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌загрузка данных (функция из задания 4)
📌вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве
 используйте магический метод проверки на равенство пользователей. Если такого пользователя нет,
 вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
 📌добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня
  доступа.
"""
from Seminar_13.task4 import *


class Loger:
    db = {}

    def __init__(self, path):
        self.__class__.db = load_json(path)
        self.level = None

    def authorize(self, the_id, name):
        if str(the_id) in self.__class__.db.keys():
            if self.__class__.db[str(the_id)]['name'] == name:
                self.level = self.__class__.db[str(the_id)]['level']
                return self.level
            else:
                raise Exception('Пользователь с такими данными не найден')
        else:
            raise Exception('Пользователь с такими данными не найден')


if __name__ == '__main__':
    PATH = 'my_user.json'
    loger = Loger(PATH)
    print(f"Уровень доступа: {loger.authorize(1, 'Сергей')}")


