from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, title='clothes'):
        self.size = size
        self.title = title

    def __str__(self):
        return f'Размер одежды "{self.title}" = {self.size}'

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return 2 * self.size + 0.3


x = Coat(25, 'H&M')
print(x), print(x.consumption)
