class InvalidNameError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid name: . Name should be a non-empty string.'


class InvalidAgeError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid age: {self.text}. Age should be a positive integer.'


class InvalidIdError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'{self.text} должен быть целым числом'


class Person:
    def __init__(self, family, name, fa_name, age):
        self.family = self.check_text(family)
        self.name = self.check_text(name)
        self.fa_name = self.check_text(fa_name)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self.age = age

    def check_text(self, text):
        if not isinstance(text, str) or not text.isalpha() or len(text) == 0:
            raise InvalidNameError(text)
        else:
            return text

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, family, name, fa_name, age, id):
        super().__init__(family, name, fa_name, age)
        if not isinstance(id, int) or 100000 < id < 1000000:
            raise InvalidIdError(id)
        self.id = id

    def get_level(self):
        sum_id = [int(i) for i in str(self.id)]
        return sum(sum_id) % 7


person = Person("", "John", "Doe", 30)