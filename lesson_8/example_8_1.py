class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def conversion(cls, user_date):
        return [int(i) for i in Date(user_date).date.split('-')]

    @staticmethod
    def validation(user_date):
        if 31 < Date.conversion(user_date)[0] or Date.conversion(user_date)[0] < 1:
            return 'Ошибка! Неверное число!'
        elif 1 > Date.conversion(user_date)[1] or Date.conversion(user_date)[1] > 12:
            return 'Ошибка! Неверный месяц!'
        elif 0 > Date.conversion(user_date)[2] or Date.conversion(user_date)[2] > 2020:
            return 'Ошибка! Неверный год!'
        return f'{".".join([str(j) for j in Date.conversion(user_date)])}'


print(*Date.conversion('12-03-1986'))
print(Date.validation('12-03-1986'))
