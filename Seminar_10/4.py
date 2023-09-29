"""
📌Создайте класс Сотрудник.
📌Воспользуйтесь классом человека из прошлого задания.
📌У сотрудника должен быть: шестизначный идентификационный номер
 уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
import random

from zad3 import People

class Sotr(People):

    def __init__(self, *args):
        super().__init__(*args)
        self.id = str(random.randint(100000, 999999))
        self.lvl = sum(list(map(int, self.id))) % 7


w = Sotr('Савочкин', 'Сергей', 'Дмитриевич', 20)
print(f'{w.full_name()}\n {w.lvl = } {w.id = }')
