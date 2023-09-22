# ✔Функция получает на вход список чисел и два индекса.
# ✔Вернуть сумму чисел между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def funk(a, b, c):
    return sum([a[i] for i in range(b, c) if c <= len(a) and b >= 0])

print(funk([1, 2, 3, 4, 5, 6], 1, 10))