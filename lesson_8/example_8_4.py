class Warehouse:
    printers, scanners, xerox = [], [], []

    @staticmethod
    def search(el_list, el):
        for i in el_list:
            if i[1]['имя'] == f'{el.title} - {el.model}' and i[1]['тип'] == f'{el.mode}' \
                    and i[1]['скорость'] == f'{el.speed}':
                return i
            else:
                return None

    @staticmethod
    def push_el():
        x = None
        while True:
            which_device = input('Какое устройство вы хотите добавить?\n1) Принтер 2) Сканер 3) Ксерокс\n-> ').lower()
            while True:
                sum_device = input('Какое количество вы хотите удалить из склада? - ')
                try:
                    int(sum_device)
                except ValueError:
                    print('Количество необходимо вводить цифрами!')
                    continue
                break
            if which_device == '1' or which_device == 'принтер':
                x = Printer()
                if Warehouse.search(Warehouse.printers, x) == None:
                    Warehouse.printers += [[len(Warehouse.printers) + 1, {'имя': f'{x.title} - {x.model}',
                                                                          'тип': x.mode, 'скорость': x.speed,
                                                                          'количество': int(sum_device)}]]
                else:
                    Warehouse.search(Warehouse.printers, x)[1]['количество'] += int(sum_device)

            elif which_device == '2' or which_device == 'сканер':
                x = Scanner()
                if Warehouse.search(Warehouse.scanners, x) == None:
                    Warehouse.scanners += [[len(Warehouse.scanners) + 1, {'имя': f'{x.title} - {x.model}',
                                                                          'тип': x.mode, 'скорость': x.speed,
                                                                          'количество': int(sum_device)}]]
                else:
                    Warehouse.search(Warehouse.scanners, x)[1]['количество'] += int(sum_device)
            elif which_device == '3' or which_device == 'ксерокс':
                x = Xerox()
                if Warehouse.search(Warehouse.xerox, x) == None:
                    Warehouse.xerox += [[len(Warehouse.xerox) + 1, {'имя': f'{x.title} - {x.model}',
                                                                    'тип': x.mode, 'скорость': x.speed,
                                                                    'количество': int(sum_device)}]]
                else:
                    Warehouse.search(Warehouse.xerox, x)[1]['количество'] += int(sum_device)
            else:
                print('Данное устройство не найдено!')
                continue
            return print('устройство добавлено')

    @staticmethod
    def pop_el():
        while True:
            which_device = input('Какое устройство вы хотите удалить?\n1) Принтер 2) Сканер 3) Ксерокс\n-> ').lower()
            while True:
                sum_device = input('Какое количество вы хотите удалить из склада? - ')
                try:
                    int(sum_device)
                except ValueError:
                    print('Количество необходимо вводить цифрами!')
                    continue
                break
            if which_device == '1' or which_device == 'принтер':
                x = Printer()
                if Warehouse.search(Warehouse.printers, x) == None:
                    print('Такого оборудования на складе нет!')
                else:
                    Warehouse.search(Warehouse.printers, x)[1]['количество'] -= int(sum_device)

            elif which_device == '2' or which_device == 'сканер':
                x = Scanner()
                if Warehouse.search(Warehouse.scanners, x) == None:
                    print('Такого оборудования на складе нет!')
                else:
                    Warehouse.search(Warehouse.scanners, x)[1]['количество'] -= int(sum_device)
            elif which_device == '3' or which_device == 'ксерокс':
                x = Xerox()
                if Warehouse.search(Warehouse.xerox, x) == None:
                    print('Такого оборудования на складе нет!')
                else:
                    Warehouse.search(Warehouse.xerox, x)[1]['количество'] -= int(sum_device)
            else:
                print('Данное устройство не найдено!')
                continue
            return print(f'устройство удалено!')


class OfficeEquipment:
    def __init__(self):
        self.title = input('Введите название фирмы-производителя - ')
        self.model = input('Введите название модели - ')
        self.mode = input('Введите тип работы (цветной/чёрно-белый) - ')


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed = input('Введите скорость печати - ')


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed = input('Введите скорость сканирования - ')


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed = input('Введите скорость копирования - ')


while True:
    print(f'{"-"*5}Склад оргтехники{"-"*5}\n'
          f'\nВы можете: 1)Добавлять 2)Удалять 3)Искать 4)Просматривать элементы на складе'
          f'\nДля выхода введите "q"\n')
    step_1 = input('Введите номер действия - ')
    if step_1 == 'q':
        print('Выполнен выход')
        break
    if step_1 == '1':
        Warehouse.push_el()
    if step_1 == '2':
        Warehouse.pop_el()
    if step_1 == '3':
        search_dev = input('Какое устройство вы хотите найти?\n1)Принтер 2)Сканер 3)Ксерокс\n-> ').lower()
        if search_dev == '1' or search_dev == 'принтер':
            x = Printer()
            if Warehouse.search(Warehouse.printers, x) == None:
                print('Такого оборудования на складе нет!')
            else:
                print(Warehouse.search(Warehouse.printers, x))
        elif search_dev == '2' or search_dev == 'сканер':
            x = Scanner()
            if Warehouse.search(Warehouse.scanners, x) == None:
                print('Такого оборудования на складе нет!')
            else:
                print(Warehouse.search(Warehouse.scanners, x))
        elif search_dev == '3' or search_dev == 'ксерокс':
            x = Xerox()
            if Warehouse.search(Warehouse.xerox, x) == None:
                print('Такого оборудования на складе нет!')
            else:
                print(Warehouse.search(Warehouse.xerox, x))
        else:
            print('Данное устройство не найдено!')
    if step_1 == '4':
        search_dev = input('Какие устройства вы хотите просмотреть?\n1)Принтеры 2)Сканеры 3)Ксероксы\n-> ').lower()
        if search_dev == '1' or search_dev == 'принтер':
            for i in Warehouse.printers:
                print(i)
        elif search_dev == '2' or search_dev == 'сканер':
            for i in Warehouse.scanners:
                print(i)
        elif search_dev == '3' or search_dev == 'ксерокс':
            for i in Warehouse.xerox:
                print(i)
        else:
            print('Данное устройство не найдено!')
    else:
        print('Данное действие не найдено!')

