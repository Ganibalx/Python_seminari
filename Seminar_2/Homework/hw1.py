def number(a):
    match a:
        case 10:
            result = 'A'
        case 11:
            result = 'B'
        case 12:
            result = 'C'
        case 13:
            result = 'D'
        case 14:
            result = 'E'
        case 15:
            result = 'F'
        case _:
            result = a
    return result

x = int(input('Введи число:\n'))
p = x
result = list()
while x > 15:
    result.append(number(x % 16))
    x = x // 16
result.append(number(x))
print(*reversed(result), sep='')
print(hex(p)[2::])
