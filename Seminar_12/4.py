"""
📌Доработайте класс прямоугольник из прошлых семинаров.
📌Добавьте возможность изменять длину и ширину прямоугольника
и встройте контроль недопустимых значений (отрицательных).
📌Используйте декораторы свойств.
"""
from functools import total_ordering

class Storona:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def _validate(self, value):
        if not(self.min_value < value < self.max_value):
            raise TypeError(f'Значение {value} не попадает в размерность')
        return value


class Prymougol:
    """
    Класс прямоугольник
    """
    width = Storona(10, 100)
    heigth = Storona(10, 100)

    def __init__(self, a, b=0):
        self.width = a
        self.heigth = b if b != 0 else a


    def __str__(self):
        return f'{self.width} {self.heigth}'


p = Prymougol(11)
p2 = Prymougol(30, 50)
print(p)
print(p2)
