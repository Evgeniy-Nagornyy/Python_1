class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def calc(self):
        return f'Масса асфальта = {self._length * self._width * 25 * 5 // 1000}т.'


x = Road(20, 5000)
print(x.calc())
