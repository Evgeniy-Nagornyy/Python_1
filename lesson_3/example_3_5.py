def num_sum(numbers=None):
    result = []
    while True:
        numbers = input('Для выхода введите любой символ не являющийся цифрой\n'
                        'Вводите цифры через пробел - ').split()
        for i in numbers:
            try:
                float(i)
            except ValueError:
                print('Выход')
                return f'Сумма вводимых чисел = {sum(result)}'
            else:
                result += [float(i)]


print(num_sum())
