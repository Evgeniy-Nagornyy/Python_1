u_numbers = [int(i) for i in input('Введите числа через пробел - ').split()]
print([i for i in u_numbers if u_numbers.count(i) == 1])
