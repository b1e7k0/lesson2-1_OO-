# Работа с файлами
# w - write(запись, перезапись)
# a - add (дозапись)
# x - создание файла без повторения имён
# r - чтение файла

# from random import choice
# students = [11, 10, 3, 13, 7, 1, 4]
# topics = tuple(range(1,8))

# with open('results.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write('38-3 RESULTS\n') 

# while students:
#     chosen_student = choice(students)
#     name = input(f'enter name for {chosen_student}: ').title()
#     rate = input(f'topic {choice(topics)}\n enter rate for {name}: ')
#     with open('results.txt', 'a', encoding='utf-8') as file:
#         file.write(f'{name} - {rate}')
#     students.remove(chosen_student)
#     print(f'студентов осталось: {students}')


# file = open("new_file.txt", "w", encoding='utf-8')
# file.write('Бишкекб ГИКС')
# # file.close()

# with open('new_file.txt', 'w', encoding='utf-8') as file:
#     file.write('\nвторая строка 2!')

# with open('new_file1.txt', 'x', encoding='utf-8') as new_file:
#     new_file.write('123')

# from time import sleep


# with open('new_file.txt', 'r', encoding='utf-8') as file:
#     for i in file.readlines():
        # sleep()
#         print(i, end='')

#     # print(file.read())
#     print(file.readlines())

with open('results.txt', encoding='utf-8') as file:
    file.readline()
    file.readline()
    rates = [int(i) for i in file.read().split() if i.isnumeric()]
    print(sum(rates) / len(rates))
    # for i in file.readlines().split():
    #     print( i if i.isnumeric() else None)



import random

def flip_coin(n):
    results = [random.choice(['Орёл', 'Решка']) for _ in range(n)]
    return results

def write_results_to_file(results, filename='coin_flips.txt'):
    with open(filename, 'a') as file:
        for result in results:
            file.write(result + '\n')

# Пример использования:
number_of_flips = 10
coin_results = flip_coin(number_of_flips)
write_results_to_file(coin_results)
