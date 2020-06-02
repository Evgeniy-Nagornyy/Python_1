class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for i in self.matrix:
            result += ' '.join([str(j) for j in i]) + '\n'
        return f'{result}'

    def __add__(self, other):
        try:
            for k in range(len(self.matrix)):  # проверяем
                if len(self.matrix[k]) == len(other.matrix[k])  and len(self.matrix) == len(other.matrix):
                    continue
                else:
                    return 'Операция сложения определена только для матриц одного порядка!'
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))]
                           for i in range(len(self.matrix))])
        except TypeError:
            return 'Элементы матрицы должны содержать только числа!'


m1 = Matrix([[1, -5, 8], [4, 5, 6]])
m2 = Matrix([[1, 2, 3], [4, 5, 6]])
m3 = Matrix([[1, 2], [4, 5]])
m4 = Matrix([[1, -5, 0], [4, 5, '6']])
print(m1 + m2)
print(m1 + m3)  # Операция сложения определена только для матриц одного порядка!
print(m2 + m4)  # Элементы матрицы должны содержать только числа!
