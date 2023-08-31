import fractions


class MyFraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__reduction__()

    def __str__(self):
        return f'{self.a}/{self.b}'

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def __reduction__(self):
        if self.a < self.b:
            min = self.a
        else:
            min = self.b
        for i in range(2, int(min**0.5)):
            if self.a % i == 0 and self.b % i == 0:
                self.a = self.a // i
                self.b = self.b // i

    def __add__(self, other):
        if self.get_b != other.get_b:
            x = self.get_a() * other.get_b() + other.get_a() * self.get_b()
            y = self.get_b() * other.get_b()
        else:
            x = self.get_a() + other.get_a()
            y = self.get_b()
        return MyFraction(x, y)

    def __mul__(self, other):
        return MyFraction(self.get_a() * other.get_a(), self.get_b() * other.get_b())


a1 = 3
b1 = 5
a2 = 8
b2 = 9

mf1 = MyFraction(a1, b1)
mf2 = MyFraction(a2, b2)
print(mf1 + mf2, mf1 * mf2)

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f1 + f2, f1 * f2)
