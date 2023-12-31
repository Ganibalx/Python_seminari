# ✔Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔Функции bin и oct используйте для проверки своего результата,
# а не для решения. Дополнительно: ✔Попробуйте избежать дублирования
# кода в преобразованиях к разным системам счисления ✔Избегайте магических чисел
# ✔Добавьте аннотацию типов где это возможно

x = int(input('Введи число:\n'))

result = list()
while x > 1:
    result.append(x % 2)
    x = x // 2
result.append(x)
print(*reversed(result))
