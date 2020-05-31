with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
    f_list = f_obj.readlines()
    m_sum = 0  # сумма зарплат сотрудников
    print('Сотрудники получающие зарплату меньше 20 тыс. :')
    for i in range(len(f_list)):
        m_sum += float((f_list[i].split())[-1])
        if float((f_list[i].split())[-1]) < 20000:
            print((f_list[i].split())[0])
    print(f'Средняя зарплата = {m_sum / (i + 1)}')
