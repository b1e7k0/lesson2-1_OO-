# time = input('введите время суток: ').lower()

# if time == 'morning' or time =='утро':
#     print('good morning')
# elif time == 'day' or time =='день':
#     print('good afternoon')
# elif time == 'eveving' or time =='вечер':
#     print('good eveving')
# else:
#     print("i don't know")
# != - это оператор сравнение означающее "не равно"
# Инициализация переменной
# counter = 1

# # Цикл while
# while counter <= 5:
#     print(counter)
#     counter += 1  # Увеличиваем значение счетчика на 1 на каждой итерации

# print("Цикл завершен.")
# Пример 1: Итерация по списку чисел
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)

# Пример 2: Итерация по строке
# word = "Python"

# for char in word:
#     print(char)
#                   Урок№3 "Циклы"

# counter = int(input('enter counter '))
# while counter < 100:
#     answer = input('enter or stop')
#     if answer == "stop":
#         print("программа заверщена")
#         break
#     print("Geeks", counter)
#     counter -= 1
# expenses = 0
# counter = 1
# days = 7
# while counter != days:
#     print(expenses)
#     expenses += int(input('Введите расход за день: {counter}:'))
#     counter += 1

# print(f'Сумма расходов: {expenses}\n'
#       f'средний расход в день: {"%.2f" % (expenses / days)}')


# [start:stop:step]
# word = 'python'
# print(word[0:3])
# print(word[3:])
# print(word[::-1])
# print(word[::2])
# print(word[0])
# print(word[4])
# print(word[-3])
# for i in word:
#     if i == 't':
#         continue
#     print(i)
# counter = 0
# for i in range(1,8):
#     counter += int(input(f"enter exp for day {i}: "))
# print(counter)
# cash = 1000
# precent = 0.15
# yers = 5
# for yers in range(1, yers+1):
#     cash += cash * precent
#     print(f'{yers} : {'%.2f' % cash}')
# #     language
# n = int(input("введи число: "))
# length = 0
# while n > 0:
#     n //= 10  # это эквивалентно n = n // 10
#     length += 1
# print(length)


# переменная.remove("element") - удаление по значению
#  переменная.pop(index) - удаление по индексу
#  del переменная[start:stop:step] -  удаление сразу нескольких элементов
# """ List comprehension"""
#  True = 1, False = 0

# numbers = [4, 2, 7.3, 5.8, 1, 6, 99]

# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))


#  Тип данных tuple(кортеж) - создаётся как с круглыми скобками так  и без. Этот список не меняется, туда вводятся данные которые нельзя менять. Обращаться к нему можно как и к списку
# cities = 'tokmok', 'bishkek', 'kara-balta'
# print(type(cities))
# cities = list(cities) 
# кортеж с одного объекта 





#     """"Словари и множества """"

# dict(dictionary) -  словарь состоит из ключа и значения {key:value}
# student = {
#     'name' : 'Jack',
#     'age' : 19,
#     'surname' : 'Walker'
# }
# print(tipe(student))
# Правила в словаре : ключами в словаре могут быть неизменяемые типы данных, значенеим может быть люой тип данных; 
# print(student['name'])
# print(student['age'])
#  enumerate() - автоматически нумерует словарь
# new = dict(name='Azamat', age=20, country= 'KG') 
# - так можно создавать словарь
# print(new)
# student['height'] = 1.76 / student['maried'] = True  - так можно добавлять ключ
# student['clothes'] - ['sweater', 'shirt', 'boots']
# student['age'] += 1
# student['name'] = 'John'
# student.update(new) - совмещает словари на новый
# del student['surename'] - удаляет объект в словаре
# student.pop('age')  - может удалять и возвращать значения
# for i in student:
#     print(i, student[i])
# print(student.keys()) - выводит только ключи
# print(student.values()) - выводит только значения
# print(student.items()) - выводит ключ и значение по парам(но это будет некрасиво)
# for key, value in student.items():
#     print(key, ':', value) - более красивый вид метода items()
#  """домашка 1 со вловарём"""
# expenses = {i: int(input(f'enter exp: for {i}')) for i in range(1, 8)}
# for day, expense in expenses.items():
#     print(f'{day}: {expense}')

# print(sum(expenses.values()) / len(expenses))
# numers = [1, 2, 3, 2, 1, 4, 5, 3]
# nubers2 = {1, 2, 3, 2, 1, 4, 5, 3}

# print(numers)
# print(type(nubers2))
# set - множители: в нём храняться данные которые могут быть уникальными и не могут повторяться между собой, изменяемый тип данных
# lagman = {'лапша', 'мясо', 'перец'}
# manty = {'тесто', 'мясо', 'лук'}
# print(lagman.difference(manty)) - выводит список без повторяющегося элемента
# print(lagman.symmetric_difference(manty))
# print(lagman.union(manty))
# print(lagman.intersection(manty))