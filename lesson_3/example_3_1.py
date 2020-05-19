def f_div(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return 'Ошибка - деление на 0'
    else:
        return f'Ответ = {result:.2f}'


print(f_div(float(input('Введите делимое - ')), float(input('Введите делитель - '))))
