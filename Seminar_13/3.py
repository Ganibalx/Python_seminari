"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""
class MyEx(Exception):
    def __init__(self, msg):
        self.message=msg

    def __str__(self):
        return f'Мое исключение: {self.message}'


class LevelError(MyEx):
    def __init__(self, msg):
        super().__init__(msg)


class AccertError(MyEx):
    def __init__(self, msg):
        super().__init__(msg)


raise LevelError('Уровень доступа меньше 7')