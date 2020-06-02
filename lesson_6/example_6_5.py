class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return '\033[34m\033[3mПишем ручкой.\033[0m'


class Pencil(Stationery):
    def draw(self):
        return '\033[35mПишем карандашом.\033[0m'


class Handle(Stationery):
    def draw(self):
        return '\033[33m\033[1mПишем маркером.\033[0m'


pen, pencil, handle = Pen('Ручка'), Pencil('Карандаш'), Handle('Маркер')
print(f'{pen.draw()} - {pencil.draw()} - {handle.draw()} ')