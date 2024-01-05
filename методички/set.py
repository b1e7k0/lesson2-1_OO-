# Создание множества
my_set = {1, 2, 3, 4, 5}

# add(x): Добавление элемента в множество
my_set.add(6)
print("After adding 6:", my_set)  # Вывод: {1, 2, 3, 4, 5, 6}

# update(iterable): Обновление множества элементами из другого итерируемого объекта
my_set.update({5, 6, 7, 8})
print("After updating with {5, 6, 7, 8}:", my_set)  # Вывод: {1, 2, 3, 4, 5, 6, 7, 8}

# remove(x): Удаление элемента из множества; вызывает ошибку, если элемент отсутствует
my_set.remove(6)
print("After removing 6:", my_set)  # Вывод: {1, 2, 3, 4, 5, 7, 8}

# discard(x): Удаление элемента из множества; не вызывает ошибку, если элемент отсутствует
my_set.discard(8)
print("After discarding 8:", my_set)  # Вывод: {1, 2, 3, 4, 5, 7}

# pop(): Удаление и возврат произвольного элемента из множества
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After popping one element:", my_set)

# clear(): Очищение множества, удаляя все его элементы
my_set.clear()
print("Cleared set:", my_set)  # Вывод: set()

# Математические операции с множествами
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union:", union_set)  # Вывод: {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Вывод: {4, 5}

difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)  # Вывод: {1, 2, 3}

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Вывод: {1, 2, 3, 6, 7, 8}
