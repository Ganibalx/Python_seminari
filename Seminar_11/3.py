"""
📌Дорабатываем класс прямоугольник из прошлого семинара.
📌Добавьте возможность сложения и вычитания.
📌При этом должен создаваться новый экземпляр прямоугольника.
📌Складываем и вычитаем периметры, а не длинну и ширину.
📌При вычитании не допускайте отрицательных значений.
"""
from functools import total_ordering


@total_ordering
class Prymougol:
    """
    Класс прямоугольник
    """
    def __init__(self, a, b=0):
        self.a = a
        self.b = b if b != 0 else a

    def perim(self):
        return 2 * (self.a + self.b)

    def plosh(self):
        return self.a * self.b

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
print(p + p2)
print(p2 - p)

print(p == p2)
print(p > p2)
print(p < p2)
print(p != p2)
print(p >= p2)
print(p <= p2)
