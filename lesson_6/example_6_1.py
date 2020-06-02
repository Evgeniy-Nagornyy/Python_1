from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        for i in cycle(self.__color):
            if i == 'Красный':
                print(f'\033[31m{i}')
                sleep(7)
            elif i == 'Зеленый':
                print(f'\033[32m{i}')
                sleep(7)
            else:
                print(f'\033[33m{i}')
                sleep(2)


x = TrafficLight()
x.running()
