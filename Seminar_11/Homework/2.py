class Archive:
    instance = None

    def __new__(cls, text, numder):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.archive_text = []
            cls.instance.archive_number = []
        else:
            cls.instance.archive_text.append(cls.instance.text)
            cls.instance.archive_number.append(cls.instance.number)
        cls.instance.number = numder
        cls.instance.text = text
        return cls.instance

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'{self.number} {self.text}'


a = Archive('Запись 1', 45)
b = Archive('Запись 2', 3.14)

print(a)