from random import randint

with open('text_5.txt', 'w+') as f_obj:
    print(*[randint(1, 100) for i in range(20)], file=f_obj)
    f_obj.seek(0)
    print(f'Сумма чисел = {sum([int(i) for i in (f_obj.readlines()[0].split())])}')
