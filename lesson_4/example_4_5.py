from functools import reduce


def sum_num(num_1, num_2):
    return num_1 * num_2


print(reduce(sum_num, [i for i in range(100, 1001) if i % 2 == 0]))
