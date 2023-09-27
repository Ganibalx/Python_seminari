"""
📌Создайте декоратор с параметром.
📌Параметр - целое число, количество запусков декорируемой функции.
"""

def outer(count):
    def decor(func):
        res=[]
        def wrapper(*args, **kwargs):
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res
        return wrapper
    return decor

@outer(5)
def func(a, b):
    return a + '_' + b

print(func('Первая', 'Вторая'))
print(func(a='Попытка', b='Два'))
print(func('Третья', b='пфытка'))