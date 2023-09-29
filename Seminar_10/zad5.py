"""
📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""
class Animals:
    def __init__(self, name):
        self.name = name
        self.spec = None

    def get_spec(self):
        return f'{self.name} - {self.spec}'


class Riba(Animals):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec


class Ptica(Animals):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec


class Ejik(Animals):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec


if __name__ == '__main__':
    r = Riba('Золотая', 'Речка')
    p = Ptica('Феникс', 'Летает')
    e = Ejik('Колючка', 'Какает')
    for pet in [r, p, e]:
        print(pet.get_spec())


