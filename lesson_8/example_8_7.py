class ComplexNumbers:
    def __init__(self, c_number):
        self.c_number = c_number.split()

    def __str__(self):
        return f'{" ".join( str(i) for i in self.c_number)}'

    def __add__(self, other):
        return ComplexNumbers(f'{int(self.c_number[0]) + int(other.c_number[0])} + '
                              f'{int(self.c_number[-1][:-1]) + int(other.c_number[-1][:-1])}i')

    def __mul__(self, other):
        a, b = int(self.c_number[0]), int(self.c_number[-1][:-1])
        c, d = int(other.c_number[0]), int(other.c_number[-1][:-1])
        return ComplexNumbers(f'{(a * c - b * d)} + {(a * d + b * c)}i')


x = ComplexNumbers('2 + 2i')
x2 = ComplexNumbers('1 + 1i')
print(x + x2)
print(x * x2)
