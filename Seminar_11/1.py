"""
📌Создайте класс Моя Строка, где:
📌будут доступны все возможности str
📌дополнительно хранятся имя автора строки и время создания (time.time)
"""
from time import time

class MyString(str):
    def __new__(cls, author, value):
        instance = super().__new__(cls, value)
        return instance

    def __init__(self, author, value):
        self.author = author
        self.c_time = time()


s = MyString('Сергей', 'Строка')
print(s.c_time)
