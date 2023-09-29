from Seminar_10.zad5 import *


class Factory:
    __class_dict = {0: Riba,
                    1: Ptica,
                    2: Ejik}

    def get_class(self, class_id, name, spec):
        return self.__class_dict[class_id](name, spec)


f = Factory()
r = f.get_class(0, 'Рыбка красная', 'Плавает')
print(r.get_spec())
p = f.get_class(1, 'Птичка синичка', 'Летает')
print(p.get_spec())
e = f.get_class(2, 'Ежик', 'Ест яблоки')
print(e.get_spec())
