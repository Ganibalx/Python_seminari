# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

a = (1, 2, 'sad', {1, 2, 3}, ['a', 'b'], 0.75, True)

b = dict()
for i in a:
    b[type(i)] = i
print(b)