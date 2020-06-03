class Cell:
    def __init__(self, sum_cell=0, len_str=5):
        self.sum_cell = int(sum_cell)  # Количество ячеек клетки
        self.len_str = len_str  # длина строки для вывода make_order

    def __str__(self):
        return f'Количество ячеек клетки = {self.sum_cell}'

    def __add__(self, other):
        return Cell(self.sum_cell + other.sum_cell)

    def __sub__(self, other):
        if self.sum_cell < other.sum_cell:
            return 'Разность количества ячеек двух клеток меньше нуля!'
        else:
            return Cell(self.sum_cell - other.sum_cell)

    def __mul__(self, other):
        return Cell(self.sum_cell * other.sum_cell)

    def __truediv__(self, other):
        return Cell(self.sum_cell // other.sum_cell)

    @property
    def make_order(self):
        pr_cell = ['*' for i in range(self.sum_cell)]
        for i in range(0, self.sum_cell, self.len_str):
            if i == 0:
                continue
            pr_cell[i] = '\n*'
        return ''.join([i for i in pr_cell])


x1 = Cell(12, 5)
x2 = Cell(4)
print(x1 * x2)
print(x1.make_order)
print(x2 - x1)
