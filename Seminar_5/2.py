# ✔Самостоятельно сохраните в переменной строку текста.
# ✔Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔Напишите преобразование в одну строку.

text = 'тут будет результирующий словарь'
print({i: ord(i) for i in text})