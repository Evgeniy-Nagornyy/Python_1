def my_func(num_1, num_2, num_3):
    num_list = [num_1, num_2, num_3]
    num_list.remove(min(num_list))
    return f'Сумма наибольших двух аргументов = {sum(num_list)}'


print(my_func(float(input('Введите 1 аргумент - ')), float(input('Введите 2 аргумент - ')),
              float(input('Введите 3 аргумент - '))))
