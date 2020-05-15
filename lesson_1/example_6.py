a = int(input('Введите результат пробежки в первый день - '))
b = int(input('Какого результата необходимо достичь? - '))
result = a
day = 1

while result < b:
    result += result * 0.1
    day += 1
    print(f'{day}-й день: {result:.2f}км')
print(f'\nНа {day}-й день спортсмен достиг результата — не менее {b} км.')
