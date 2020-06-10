class NoZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    num1 = int(input('Введите делимое - '))
    num2 = int(input('Введите делитель - '))
    if num2 == 0:
        raise NoZero('Деление на 0!')
except NoZero as err:
    print(err)
except ValueError:
    print('Вводить только числа!')
else:
    print(f'{num1} / {num2} = {num1 / num2}')
