# Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

a = [1, 2, 3, 1, 2, 3, 1]

i = 0
while i < len(a):
    item = a[i]
    while a.count(item) > 1:
        if a.count(item) >= 2:
            a.remove(item)
        a.remove(item)
        i = i - 1
    i = i + 1
print(a)