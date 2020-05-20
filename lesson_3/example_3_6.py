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

    for k in range(len(result)):  # в каждом слове делаем с заглавной буквы.
        for p in range(len(result[k])):  # str.title увы не подходит... должен быть более короткий вариант
            if p == 0:
                result_end += result[k][p].upper()
            else:
                result_end += result[k][p]
        result_end += ' '

    return result_end


print(int_func(input('Введите слова через пробел - ').split(), True))
