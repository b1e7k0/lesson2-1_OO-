# Создание кортежа
my_tuple = (1, 2, 3)

# index(x): Возвращает индекс первого вхождения элемента x
index_of_2 = my_tuple.index(2)
print("index of 2:", index_of_2)  # Вывод: 1

# count(x): Возвращает количество вхождений элемента x
count_of_3 = my_tuple.count(3)
print("count of 3:", count_of_3)  # Вывод: 1

# Объединение кортежей
another_tuple = (4, 5, 6)
combined_tuple = my_tuple + another_tuple
print("combined tuple:", combined_tuple)  # Вывод: (1, 2, 3, 4, 5, 6)

# Распаковка кортежа
a, b, c = my_tuple
print("Unpacked values:", a, b, c)  # Вывод: 1 2 3

# Доступ к элементам по индексу
element_at_index_1 = my_tuple[1]
print("Element at index 1:", element_at_index_1)  # Вывод: 2

# Проверка вхождения элемента
is_element_present = 3 in my_tuple
print("Is 3 present:", is_element_present)  # Вывод: True

# Длина кортежа
length_of_tuple = len(my_tuple)
print("Length of tuple:", length_of_tuple)  # Вывод: 3

# Создание кортежа из списка
list_to_tuple = tuple([7, 8, 9])
print("Tuple from list:", list_to_tuple)  # Вывод: (7, 8, 9)
