numbers_list = [7, 5, 3, 3, 2]  # задаем список в который будем добавлять цифры

while True:
    u_num = input('Для выхода введите "end"\nВведите число - ')
    if u_num == 'end':
        break  # выход из программы если пользователь ввел 'end'
    else:
        u_num = int(u_num)  # преобразуем ответ пользователя в int
        for i in range(len(numbers_list)):  # ищем место для цифры в списке
            if u_num > numbers_list[i]:
                numbers_list.insert(i, u_num)  # вставляем ответ пользователя перед цифрой меньше
                break
            elif i == len(numbers_list) - 1:  # если цифра самая маленькая из списка, то добавляем в ее конец
                numbers_list.append(u_num)
    print(f'Рейтинг - {numbers_list}')
