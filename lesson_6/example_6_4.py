class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        return f'({self.name}) начало движения'

    def stop(self):
        return f'({self.name}) остановка'

    def turn(self, direction):
        return f'({self.name}) поворот на {direction}'

    def show_speed(self):
        return f'({self.name}) Скорость = {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\033[31m({self.name}) Скорость {self.speed}\nПревышение скорости на {self.speed - 60}\033[0m'
        else:
            return f'({self.name}) Скорость = {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\033[31m({self.name}) Скорость {self.speed}\nПревышение скорости на {self.speed - 40}\033[0m'
        else:
            return f'({self.name}) Скорость = {self.speed}'


class PoliceCar(Car):
    pass


sport_car = SportCar(100, "red", 'Mazda RX8')
work_car = WorkCar(90, 'Blue', 'bus')
police_car = PoliceCar(60, 'white', 'ВАЗ', True)
print(police_car.is_police)
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn('Право'))
print(work_car.go())
print(work_car.show_speed())
print(work_car.stop())
print(sport_car.stop())
