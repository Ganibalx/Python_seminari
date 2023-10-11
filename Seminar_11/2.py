"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌При нового экземпляра класса, старые данные из ранее созданных экземпляров
 сохраняются в пару списковархивов 📌list-архивы также являются свойствами экземпляра
"""
class Arhive:
    zip_lst = []

    def __new__(cls, value, text):
        instance = super().__new__(cls)
        instance.value = value
        instance.text = text
        instance.arch = cls.zip_lst.copy()
        cls.zip_lst.append(instance)
        return instance

    def __str__(self):
        return f'{self.value} {self.text} | {self.arch}'

    def __repr__(self):
        return f'{self.value} {self.text}'


a = Arhive(1, 'a')
b = Arhive(2, 'b')

print(b)
