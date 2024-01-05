"""1 Задание"""

numbers = [312, 996, 31, 1991]
target_nuber = 1000
nearest_number = sorted(numbers, key=lambda x: abs(x - target_nuber))
print((target_nuber, nearest_number))


"""2 Задание"""

names = ['Bekzat', 'Bolot', 'Baha', 'Shaha', 'Aku']


def find_names(iterable):
    while True:
        print(iterable)
        index_n = input('Введите индекс имени или "Выход": ')
        if index_n == 'Выход':
            break
        else:
            try:
                index_n = int(index_n)
                print(f' Имя по введённому индексу {index_n} : {iterable[index_n]}')
            except IndexError:
                print(f'Вводить можно только числа от 0 до {len(iterable) - 1}!')
            except ValueError:
                print('Вводить можно только цифры!')

print(find_names(names))

"""3 Задание"""

cars = [
    {"marka": "BMW", "country": "Germany"},
    {"marka": "Toyota", "country": "Japan"},
    {"marka": "Mers", "country": "Germany"},
    {"marka": "Subaru", "country": "Jjapan"},
    ]

filtered_cars = list(filter(lambda x: x["country"] == "Germany", cars))
print(filtered_cars)

mapped_cars = list(map(lambda x: x.get("marka"), cars))
print(mapped_cars)