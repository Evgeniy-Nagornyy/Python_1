user_list = input('Введите элементы через пробел - ').split()

for i in range(0, len(user_list), 2):
    user_list.insert(i + 2, user_list[i])
    user_list.pop(i)

print(user_list)
