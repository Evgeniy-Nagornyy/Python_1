list_type = [23, 2.3, complex(1, 2), bytes(1), bytearray(1), 'строка', None, False,
             [1, 2], (3, 4), {1, 2, 'строка'}, {'имя': 'john'}]

for i in range(len(list_type)):
    print(f'{i + 1}: {list_type[i]} -----> {type(list_type[i])}')
