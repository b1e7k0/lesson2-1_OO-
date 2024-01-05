left = 1
right = 100
attempts = []
while True:
    middle = int((left + right) / 2)
    print(f'Загаданное число {middle}?')
    attempts.append(middle)
    answer = input('да, больше, меньше: ')
    if answer == 'да':
        print("Число угадано!")
        with open("results.txt", 'w', encoding='utf-8') as file:
            file.write(f'Количество попыток: {len(attempts)}\n')
            file.write(f'Список попыток: {attempts}\n')
            file.write(f'Загаданное число: {middle}')
        break
    elif answer == "больше":
        left = middle + 1
    elif answer == "меньше":
        right = middle - 1
    else:
        print("Команда неопозднана")
