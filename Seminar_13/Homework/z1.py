from functools import total_ordering


class NegativeValueError(Exception):
    def __init__(self, value, text):
        self.value = value
        self.text = text

    def __str__(self):
        return f'{self.text} должна быть положительной, а не {self.value}'


@total_ordering
class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self, a, b=0):
        self._width = self.check(a, 'Ширина')
        self._height = self.check(b, 'Высота')

    def check(self, value, text):
        if (type(value) == int or type(value) == float) and value > 0:
            return value
        else:
            raise NegativeValueError(value, text)

    def perimeter(self):
        return int(2 * (self.width + self.height))

    def area(self):
        return int(self.width * self.height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = self.check(value, 'Ширина')

    @height.setter
    def height(self, value):
        self._height = self.check(value, 'Высота')

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


if __name__ == '__main__':
    # a = Rectangle(4, 5)
    # a.height = 6
    # a.width = 6
    # print(a)

    r = Rectangle(5, -3)