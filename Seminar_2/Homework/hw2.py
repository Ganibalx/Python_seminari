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


class MyCalculate:
    def __init__(self, fraction_a, fraction_b):
        self.fraction_a = fraction_a
        self.fraction_b = fraction_b

    def get_sum(self):
        if self.fraction_a.get_b != self.fraction_b.get_b:
            x = self.fraction_a.get_a() * self.fraction_b.get_b() + self.fraction_b.get_a() * self.fraction_a.get_b()
            y = self.fraction_a.get_b() * self.fraction_b.get_b()
        else:
            x = self.fraction_a.get_a() + self.fraction_b.get_a()
            y = self.fraction_a.get_b()
        return MyFraction(x, y)

    def get_comp(self):
        x = self.fraction_a.get_a() * self.fraction_b.get_a()
        y = self.fraction_a.get_b() * self.fraction_b.get_b()
        return MyFraction(x, y)


a1 = 3
b1 = 5
a2 = 8
b2 = 9

calc = MyCalculate(MyFraction(a1, b1), MyFraction(a2, b2))
print(calc.get_sum(), calc.get_comp())

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f1 + f2, f1 * f2)
