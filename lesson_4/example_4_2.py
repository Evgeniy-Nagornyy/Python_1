u_numbers = [int(i) for i in input('Введите числа через пробел - ').split()]
print([u_numbers[i] for i in range(1, len(u_numbers)) if u_numbers[i] > u_numbers[i - 1]])
