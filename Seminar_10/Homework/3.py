class Matrix:
    def __init__(self, a, b):
        if a and b:
            self.a = a
            self.b = b
            self.set_m()
        else:
            raise Exception('Ну из этого ничего не сделать')

    def set_m(self, list_z=None):
        if list_z and len(list_z) == self.a * self.b:
            l_gen = (g for g in list_z)
            self.m = [[next(l_gen) for j in range(self.a)] for i in range(self.b)]
        elif not list_z:
            self.m = [[0 for j in range(self.a)] for i in range(self.b)]
        else:
            raise 'Мало'

    def __str__(self):
        rstr = ''
        for i in self.m:
            rstr = rstr + str(i) + '\n'
        return rstr


m = Matrix(3, 5)
print(m)
m.set_m([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(m)