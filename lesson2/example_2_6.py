product = []  # база данных
i = 0  # счетчик для учета позиций

while True:
    step_1 = input('Хотите добавить товар?\n"yes"/"no" - ').lower()
    if step_1 == 'yes':
        product += [(i + 1, {'название': None, 'цена': None, 'количество': None, 'ед': None})]  # создаем базу
        product[i][1]['название'] = input('Введите название продукта - ')
        product[i][1]['цена'] = input('Введите цену продукта - ')
        product[i][1]['количество'] = input('Введите его количество - ')
        product[i][1]['ед'] = input('Введите единицу измерения продукта - ')
        print(f'Вы добавили - {product[i][1]}')
        i += 1
    elif step_1 == 'no':
        break

analytics = {'название': [product[j][1]['название'] for j in range(len(product))],  # генерирование аналитики
             'цена': [product[j][1]['цена'] for j in range(len(product))],
             'количество': [product[j][1]['количество'] for j in range(len(product))],
             'ед': [product[j][1]['ед'] for j in range(len(product))]
             }

base = '\n'.join(str(j) for j in product)  # переменная для вывода базы
analytics_out = '\n'.join((str(list(analytics.items())[j])) for j in range(4))  # переменная для вывода аналитики

while True:  # подобие меню
    step_2 = input(f'Для вывода базы товаров введите - "b"\n'
                   f'Для вывода аналитики введите - "a"\n'
                   f'для выхода введите - "q"\n').lower()
    if step_2 == 'b':
        print(f'{base}\n')
    elif step_2 == 'a':
        print(f'{analytics_out}\nКоличество позиций - {i + 1}\n')
    elif step_2 == 'q':
        break
