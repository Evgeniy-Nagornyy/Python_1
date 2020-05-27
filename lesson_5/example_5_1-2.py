# первое задание
with open('text_1.txt', 'w', encoding='utf-8') as f_obj:
    print('Для выхода введите пустую строку')
    while True:
        message = input('Введите строку для записи - ') + '\n'
        if len(message) == 1:
            break
        else:
            f_obj.write(message)

# второе задание
with open('text_1.txt', 'r', encoding='utf-8') as f_obj_r:
    f_list = f_obj_r.readlines()
    print(f'Количество строк в файле - {len(f_list)}')
    for i in range(len(f_list)):
        print(f'Количество слов в {i + 1} строке - {len(f_list[i].split())} шт.')
