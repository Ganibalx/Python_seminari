from functools import total_ordering


@total_ordering
class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self, a, b=0):
        self.width = a
        self.height = b if b != 0 else a

    def perimeter(self):
        return int(2 * (self.width + self.height))

    def area(self):
        return int(self.width * self.height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, self.height - other.height)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))