user_time = int(input('Введите время в секундах - '))

second = (user_time % 3600) % 60
if second < 10:  # с форматом чч:мм:сс придумал только так, иначе подключать модуль datetime.
    second = '0' + str(second)
minute = (user_time % 3600) // 60
if minute < 10:
    minute = '0' + str(minute)
hour = (user_time // 3600)
if hour < 10:
    hour = '0' + str(hour)

print(f'{hour}:{minute}:{second}')
