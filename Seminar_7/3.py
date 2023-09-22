# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def file_read():
    with open('file.txt', 'r', encoding='utf-8') as numbers:
        n = numbers.read().split('\n')
    with open('file2.txt', 'r', encoding='utf-8') as name:
        na = name.read().split('\n')
    n.pop()
    na.pop()
    if len(n) > len(na):
        na.extend(na[:len(n)-len(na)])
    elif len(na) > len(n):
        n.extend(n[:len(na)-len(n)])
    with open('file3.txt', 'a', encoding='utf-8') as result:
        for i in range(len(n)):
            a, b = n[i].split('|')
            r = int(a)*float(b)
            if r > 0:
                result.write(f'{na[i].upper()} {int(r)}\n')
            else:
                result.write(f'{na[i].lower()} {round(abs(r), 2)}\n')


file_read()
