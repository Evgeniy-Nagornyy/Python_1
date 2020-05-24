def int_func(user_list, filter=False):
    result = user_list.copy()
    result_end = ''

    if filter == True:  # фильтр, пропускаем только слова состоящие из маленьких латинских букв
        for i in range(len(user_list)):
            for j in user_list[i]:
                if ord('a') < ord(j) < ord('z'):  # проверяем буквы в слове
                    continue
                else:
                    result.remove(user_list[i])  # если обнаружено несоответствие условию, то удаляем слово
                    break

    for k in result:  # в каждом слове делаем с заглавной буквы.
        result_end += (k.replace(k[0], k[0].upper(), 1) + ' ')
    return result_end


print(int_func(input('Введите слова через пробел - ').split(), True))
