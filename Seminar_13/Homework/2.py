from typing import Union


class InvalidTextError(Exception):
    def __str__(self):
        return f'Invalid text: . Text should be a non-empty string.'


class InvalidNumberError(Exception):
    def __str__(self):
        return f'Invalid number: -5. Number should be a positive integer or float.'


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if type(text) == str and len(text) > 0:
            self.text = text
        else:
            raise InvalidTextError()
        if (type(number) == int or type(number) == float) and number > 0:
            self.number = number
        else:
            raise InvalidNumberError()

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'