line_numbers = int(input('Введите положительное число - '))
check_number = line_numbers % 10  # Проверяемое число на максимум (очень не хватает цикла do while)
check_line_number = str(check_number)  # проверочное число для выхода из цикла
max_number = 0  # Максимальное число
i = 1  # счетчик для передвижения
if line_numbers == 0:  # вдруг введут 0
    print(max_number)
else:
    while int(check_line_number) <= line_numbers:
        check_number = ((line_numbers % (10 ** i)) // (10 ** (i - 1)))  # переключение на следующую цифру
        if check_number == 9:  # проверяем, есть ли смысл проверять дальше
            max_number = check_number
            break
        elif check_number > max_number:  # проверка числа
            max_number = check_number
        check_line_number = str(check_number) + check_line_number  # формируем число для проверки выхода из цикла
        i += 1
    print(f'Самая большая цифра в числе - {max_number}')

# второй вариант решения ("запрещенный")

# line_numbers = input('Введите положительное число - ')
# print(f'Самая большая цифра в числе - {max([int(line_numbers[i]) for i in range(len(line_numbers))])}')
