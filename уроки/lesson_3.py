# Циклы.

"""while"""
# c = 0
# while c < 100:
#     answer = input('enter or stop')
#     if answer == 'stop':
#         print('программа завершена')
#         break
#     print('GEEKS', c)
#     c += 1

# counter = int(input('enter counter: '))
#
# while counter > 0:
#     time = input(f'введите время суток: {counter} ').lower()
#     if time == 'stop':
#         print('finish')
#         break
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('i don\'t know time')
#     counter -= 1


# while True:
#     temp = input('enter temperature: ')
#     if temp == 'stop':
#         break
#     temp = int(temp)
#
#     if temp < 0 and temp >= -30:
#         print('холодно')
#     elif temp >= 0 and temp <= 10:
#         print('прохладно')
#     elif temp > 10 and temp <= 23:
#         print('тепло')
#     elif temp > 23 and temp <= 40:
#         print('жарко')
#     else:
#         print('не выжить тебе!')

"""ПЕРЕРЫВ ДО 17:00"""

# expenses = 0
# counter = 1
# days = 7
# while counter != days:
#     print(expenses)
#     expenses += int(input(f'введите расход за день: {counter}: '))
#     counter += 1
#
# print(f'сумма расходов: {expenses}\n'
#       f'средний расход в день: {"%.2f" % (expenses / days)}')

# number = 45.8235782
#
# print(round(number, 2))
# print("%.2f" % number)
# [start:stop:step]


"""for"""

# cash = 1000
# percents = 0.15
# years = 5
#
# for year in range(1, years+1):
#     cash += cash * percents
#     print(f"{year}: {'%.2f' % cash}")


# counter = 0
# for i in range(1, 8):
#     counter += int(input(f'enter exp for day {i}: '))
#
# print(counter)


# word = '123456789'
# print(word[::2])
# print(word[0:3])
# print(word[3:])
# print(word[::-1])

# print(word[0])
# print(word[4])
# print(word[-1])

#
# for i in word:
#     if i == 't':
#         continue
#     print(i)

# дфтпгфпу
# ghjuhfvvbhjdfybt

# eng = "qwerty"
# rus = "йцукен"

# print(eng.index('r'))
# print(rus[3])
# print(rus[eng.index('t')])

# print('p' in 'python')
# print('u' in 'python')


# word = 'KYRGYZSTAN'
#
# print(word.index('R'))
# print(word.index('Y'))
# print(word.index('Y', 2))
