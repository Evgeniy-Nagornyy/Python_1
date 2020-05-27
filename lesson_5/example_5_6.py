with open('text_6.txt', 'r') as f_obj:
    lf_obj = f_obj.readlines()
    data_base = {}
    for i in range(len(lf_obj)):
        sum_hours = 0  # количество часов занятий
        for j in range(1, len(lf_obj[i].split())):
            if lf_obj[i].split()[j] == '-':  # если занятие отсутствует, то пропускаем
                continue
            else:  # отсеиваем лишнее от цифр и сумируем часы (срез по индексу "(")
                sum_hours += int(lf_obj[i].split()[j][:(lf_obj[i].split()[j].index('('))])
        data_base.update({(lf_obj[i].split()[0])[:-1]: sum_hours})  # добавляем значения в базу
    print(data_base)
