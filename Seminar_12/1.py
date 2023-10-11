"""
📌Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌Экземпляр должен запоминать последние k значений.
📌Параметр k передаётся при создании экземпляра.
📌Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""
import json


class Factorial:
    def __init__(self, count):
        self.count = count
        self.archive = {}

    def _fact(self, k):
        factorial = []
        num = 1
        for i in range(1, k+1):
            num *= i
            factorial.append(num)
        return factorial

    def __call__(self, k):
        result = self._fact(k)[-self.count:]
        self.archive[k] = result
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('fackt_dice.json', 'w', encoding='UTF-8')
        json.dump(self.archive, file, indent=4)
        file.close()


with Factorial(3) as f:
    print(f(7))
    print(f(6))
