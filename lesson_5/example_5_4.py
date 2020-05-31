en_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as f_obj_r:
    with open('text_4_rus.txt', 'w', encoding='utf-8') as f_obj_w:
        list_f_obj_r = f_obj_r.readlines()
        for i in range(len(list_f_obj_r)):  # редактируем и записываем построчно из "text_4" в "text_4_rus"
            print(f'{en_ru[((list_f_obj_r[i]).split())[0]]} {((list_f_obj_r[i]).split())[1]} '
                  f'{((list_f_obj_r[i]).split())[2]}', file=f_obj_w)
           