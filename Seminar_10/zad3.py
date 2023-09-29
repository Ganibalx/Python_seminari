"""
📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
 на ваш выбор. 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность
 получить текущий возраст.
"""

class People:

    def __init__(self, f, i, o, age):
        self.f = f
        self.i = i
        self.o = o
        self.age = age

    def full_name(self):
        return f'{self.f} {self.i} {self.o}'

    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1


if __name__ == '__main__':
    p = People('Савочкин', 'Сергей', 'Дмитриевич', 20)
    print(p.full_name())
    print(p.get_age())
    p.birthday()
    print(p.get_age())
