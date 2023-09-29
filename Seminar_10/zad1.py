"""
📌Создайте класс окружность.
📌Класс должен принимать радиус окружности при создании экземпляра.
📌У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi


class Circles:

    def __init__(self, r):
        self.r = r

    def lenght_c(self):
        return 2 * pi * self.r

    def plosh(self):
        return pi * (self.r ** 2)


c = Circles(4)
print(c.lenght_c())
print(c.plosh())
