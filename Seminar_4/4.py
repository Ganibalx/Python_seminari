# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

def my_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
my_sort(b)
print(b)