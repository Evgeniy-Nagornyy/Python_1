class Worker:
    def __init__(self, name, surname, position):
        dic_income = {"wage": 20000, "bonus": 10000}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dic_income


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника - {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии - {self._income["wage"] + self._income["bonus"]}'


human = Position(input("Введите имя - "), input("Введите фамилию - "), input("Введите должность - "))

print(human.get_full_name())
print(human.get_total_income())
