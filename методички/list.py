# Создание списка
my_list = [1, 2, 3]

# append(x): Добавление элемента в конец списка
my_list.append(4)
print("append:", my_list)  # Вывод: [1, 2, 3, 4]

# extend(iterable): Расширение списка другим итерируемым объектом
my_list.extend([5, 6])
print("extend:", my_list)  # Вывод: [1, 2, 3, 4, 5, 6]

# insert(i, x): Вставка элемента на позицию i
my_list.insert(1, 7)
print("insert:", my_list)  # Вывод: [1, 7, 2, 3, 4, 5, 6]

# remove(x): Удаление первого вхождения элемента x
my_list.remove(2)
print("remove:", my_list)  # Вывод: [1, 7, 3, 4, 5, 6]

# pop([i]): Удаление и возврат элемента на позиции i
removed_element = my_list.pop(2)
print("pop:", my_list)          # Вывод: [1, 7, 4, 5, 6]
print("Removed element:", removed_element)  # Вывод: 3

# index(x): Возвращение индекса первого вхождения элемента x
index_of_7 = my_list.index(7)
print("index of 7:", index_of_7)  # Вывод: 1

# count(x): Возвращение количества вхождений элемента x
count_of_4 = my_list.count(4)
print("count of 4:", count_of_4)  # Вывод: 1

# sort(): Сортировка списка
my_list.sort()
print("sort:", my_list)  # Вывод: [1, 4, 5, 6, 7]

# reverse(): Изменение порядка элементов на обратный
my_list.reverse()
print("reverse:", my_list)  # Вывод: [7, 6, 5, 4, 1]
#  замена элемента старого на новый
list = list.replace(_old: )