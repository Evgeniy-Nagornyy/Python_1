def f_dict(**kwargs):
    '''
    Функция принимает несколько параметров и выводит их в виде словаря.
    Пример: f_base(name='Иван') --> {'name': 'Иван'}
    '''
    return kwargs


print(f_dict(name=input('Введите имя - '), surname=input('Введите фамилию - '), birth=input('Введите год рождения - '),
             city=input('Введите город проживания - '), email=input('Введите email - '),
             phone=input('Введите номер телефона - ')))
