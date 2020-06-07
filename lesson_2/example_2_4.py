user_words = input('Введите слова через пробел - ').split()
for i in range(len(user_words)):
    print(f'{i + 1} - {user_words[i][:10]}')
