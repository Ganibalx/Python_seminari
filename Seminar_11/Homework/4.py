class Matrix:
    def __init__(self, a, b):
        self.rows = a
        self.cols = b
        self.data = [[0 for j in range(self.cols)] for i in range(self.rows)]

    def __str__(self):
        rstr = '\n'.join([' '.join([str(j) for j in i]) for i in self.data])
        return rstr

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if isinstance(other, Matrix):
            flag = True
            if self.rows == other.rows and self.cols == other.cols:
                for i in range(len(self.data)):
                    for j in range(len(self.data[i])):
                        if self.data[i][j] != other.data[i][j]:
                            flag = False
            else:
                flag = False
        return flag

    def __add__(self, other):
        if isinstance(other, Matrix):
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(len(new_matrix.data)):
                for j in range(len(new_matrix.data[i])):
                    new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
        return new_matrix

    def __mul__(self, other):
        new_matrix = Matrix(self.rows, other.cols)
        for i in range(len(new_matrix.data)):
            for j in range(len(new_matrix.data[i])):
                new_matrix.data[i][j] = sum([self.data[i][g] * other.data[g][j] for g in range(self.cols)])
        return new_matrix


#Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
