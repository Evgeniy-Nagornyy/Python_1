income = int(input('Введите значение выручки - '))
costs = int(input('Введите значение издержек фирмы - '))

if (income - costs) < 0:
    print(f'Убыток - {income - costs}')
elif (income - costs) > 0:
    print(f'Прибыль - {income - costs}')
    print(f'Рентабельность выручки - {(income / costs) * 100}%')
    num_employees = int(input('Введите число сотрудников - '))
    print(f'Прибыль на одного сотрудника - {(income - costs) / num_employees}')
else:
    print('Выручка равна издержке')