"""
📌Доработайте класс прямоугольник из прошлых семинаров.
📌Добавьте возможность изменять длину и ширину прямоугольника
и встройте контроль недопустимых значений (отрицательных).
📌Используйте декораторы свойств.
"""
from functools import total_ordering


@total_ordering
class Prymougol:
    """
    Класс прямоугольник
    """



    def __init__(self, a, b=0):
        self._a = a
        self._b = b if b != 0 else a

    def perim(self):
        return 2 * (self.a + self.b)

    def plosh(self):
        return self.a * self.b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise Exception('не пойдет')

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise Exception('не пойдет')

    def __add__(self, other):
        if isinstance(other, Prymougol):
            return Prymougol(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        if isinstance(other, Prymougol):
            if self.a > other.a and self.b > other.b:
                return Prymougol(self.a - other.a, self.b - other.b)

    def __str__(self):
        return f'{self.a} {self.b}'

    def __eq__(self, other):
        if isinstance(other, Prymougol):
            return self.plosh() == other.plosh()

    def __lt__(self, other):
        if isinstance(other, Prymougol):
            return self.plosh() < other.plosh()


p = Prymougol(3)
p2 = Prymougol(4, 6)
p.a = 5
p2.b = 4
print(p)
print(p2)
