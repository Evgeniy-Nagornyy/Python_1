from math import factorial

u_num = int(input('Введите целое число - '))


def fact(num):
    for i in range(1, num + 1):
        yield f'{i}!: {factorial(i)}'


for el in fact(u_num):
    print(el)
