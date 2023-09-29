class Triangle:
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
            self.__type_triangle()
        else:
            raise Exception('Треугольник не существует')

    def __type_triangle(self):
        self.type = 'Разносторонний'
        if self.a == self.b and self.b == self.c:
            self.type = 'Равносторонний'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            self.type = 'Равнобедренный'


t = Triangle(2, 3, 4)
print(t.type)
