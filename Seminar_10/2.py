"""
📌Создайте класс прямоугольник.
📌Класс должен принимать длину и ширину при создании экземпляра.
📌У класса должно быть два метода, возвращающие периметр и площадь.
📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""

class Prymougol:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b if b != 0 else a

    def perim(self):
        return 2 * (self.a + self.b)

    def plosh(self):
        return self.a * self.b


p = Prymougol(3)
p2 = Prymougol(4, 6)
print(p.plosh(), p.perim())
print(p2.plosh(), p2.perim())
