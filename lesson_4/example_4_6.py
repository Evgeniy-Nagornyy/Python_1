from itertools import count, cycle
start = int(input('Введите нижнюю границу генерирования  - '))
end = int(input('Введите вверхнюю границу генерирования  - '))
new_list = []

for i in count(start):
    if i > end:
        break
    else:
        new_list += [i]

print(*new_list)
z = 0

for j in cycle(new_list):
    if z >= len(new_list) * 2:
        break
    else:
        print(j, end=' ')
        z += 1
