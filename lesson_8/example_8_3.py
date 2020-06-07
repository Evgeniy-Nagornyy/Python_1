class NoNumber(Exception):
    def __init__(self, text):
        self.text = text


result = []
while True:
    user_el = input('Для выхода введите "stop"\nВведите элементы списка через пробел - ')
    if user_el == 'stop':
        print(result)
        break

    user_el = user_el.split()
    for i in user_el:
        try:
            for j in i:
                if j in [str(z) for z in range(10)]:
                    continue
                else:
                    raise NoNumber(f'{i} не является числом!')
            result += [i]
        except NoNumber as non:
            print(non)
