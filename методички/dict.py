# Создание словаря
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# keys(): Возвращает список ключей в словаре
keys_list = my_dict.keys()
print("Keys:", keys_list)  # Вывод: ['name', 'age', 'city']

# values(): Возвращает список значений в словаре
values_list = my_dict.values()
print("Values:", values_list)  # Вывод: ['John', 25, 'New York']

# items(): Возвращает список кортежей (ключ, значение)
items_list = my_dict.items()
print("Items:", items_list)  # Вывод: [('name', 'John'), ('age', 25), ('city', 'New York')]

# get(key): Возвращает значение по ключу, None, если ключ отсутствует (или значение по умолчанию, если указано)
age = my_dict.get('age')
print("Age:", age)  # Вывод: 25

# pop(key): Удаляет и возвращает значение по ключу
city = my_dict.pop('city')
print("City:", city)  # Вывод: New York
print("Updated dict:", my_dict)  # Вывод: {'name': 'John', 'age': 25}

# update(other_dict): Обновляет словарь элементами из другого словаря или итерируемого объекта
my_dict.update({'gender': 'Male'})
print("Updated with gender:", my_dict)  # Вывод: {'name': 'John', 'age': 25, 'gender': 'Male'}

# clear(): Очищает словарь, удаляя все его элементы
my_dict.clear()
print("Cleared dict:", my_dict)  # Вывод: {}

# Создание словаря из двух списков (ключи и значения)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = dict(zip(keys, values))
print("New dictionary:", new_dict)  # Вывод: {'a': 1, 'b': 2, 'c': 3}
