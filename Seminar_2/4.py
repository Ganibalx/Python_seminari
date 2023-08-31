# ✔Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 45
x = int(input('Введите диаметр'))
if x < 1000 and x > 0:
    dlina = decimal.Decimal(math.pi) * x
    s = decimal.Decimal(math.pi) * decimal.Decimal((x/2)**2)
    print(f'{dlina}\n {s}\n')
