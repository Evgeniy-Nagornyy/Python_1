def my_func(x, y):
    return f'x в степени y = {x ** y}'


def my_func2(x, y):
    div = 1
    for i in range(-y):
        div *= x
    return f'x в степени y = {1 / div}'


print(my_func(float(input('Введите положительное число x - ')), int(input('Введите целое отрицательное число y - '))))
print(my_func2(float(input('Введите положительное число x - ')), int(input('Введите целое отрицательное число y - '))))
