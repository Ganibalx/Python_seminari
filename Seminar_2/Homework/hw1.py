NUMBER = '0123456789abcdef'

x = int(input('Введи число:\n'))
p = x
result = list()
while x > 15:
    result.append(NUMBER[x % 16])
    x = x // 16
result.append(NUMBER[x])
print(*reversed(result), sep='')

print(hex(p)[2::])
