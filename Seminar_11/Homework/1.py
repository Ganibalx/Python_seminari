from datetime import datetime

class MyStr(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.value = args[0]
        instance.author = args[1]
        instance.time = datetime.now()
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time.strftime("%Y-%m-%d %I:%M")})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


s = MyStr('Сергей', 'Строка')
print(repr(s))
