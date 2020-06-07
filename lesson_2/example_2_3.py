user_month = int(input('Введите номер месяца - '))
month_list = ['январь', 'февраль', 'Март', 'апрель', 'май', 'Июнь',
              'июль', 'август', 'Сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], ['Зима', 'Весна', 'Лето', 'Осень']]
season2version = {0: 'Зима', 1: 'Весна',
                  2: 'Лето', 3: 'Осень'}  # можно расширить библиотеку до 12 ключей и избежать цикла

for i in range(0, 4):
    for j in season[i]:
        if user_month == j:
            print(f'{user_month} месяц - {month_list[user_month - 1]} - {season[4][i]}')  # первый вариант
            print(f'{user_month} месяц - {month_list[user_month - 1]} - {season2version[i]}')  # второй вариант
