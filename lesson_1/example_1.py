user_name = input('Введите ваше имя - ')

print(f'Привет {user_name}!')

int_number = int(input('Введите целое число - '))
float_number = float(input('Введите число с плавающей запятой - '))
user_line = input('Введите ваш комментарий - ')

print(f'{user_name}\n'
      f'Ваше целое число = {int_number}\n'
      f'Ваше число с плавающей запятой = {float_number}\n'
      f'Ваш комментарий - \"{user_line}\"')
