# """Функции""": *args, **kwargs
# DRY - don't repeat yourself
# name - это обязательной позиционный параметр
# переменная="какое либо слово" - обозночает что если туда не вводится ничего то выводится по умочанию "какое либо слово"
# def get_data(name, surname="unknown"): 
#     print(f"name: {name} surname: {surname}")
# get_data("Бекзат", "Сайдуллаев")
# # "Бекзат" - обязательный позиционный аргумент
# get_data('Jack', '')
# get_data(surname="Асанов", name="Тилек")
# это ключевые аргументы
# *args - запаковывает аргументы в кортедж
# def plus(*args):
#     return sum(args)
# print(plus(6,8,5,87))
# def plus(num1, num2, num3):
#     return num1 + num2 + num3
# print(plus(6,8))
# **kwargs - запаковывает аргументы в словарь

# word  = 'kyrgyzstan'
# def len1(iterable):
#     cougt = 0
#     for _ in iterable:
#         cougt += 1
#     return cougt
# print(len1(word))

# iterable - обозночает какую то последовательность (строчки, списки, кортежи и т.д.)
# length = 7
# width = 5
# ssquare_2 = length * width
# print(ssquare_2)

# length_p = 700
# width_p = 500
# ssquare_p_2 = length_p * width_p
# print(ssquare_p_2)

# length_h = 15
# width_h = 10
# ssquare_h_2 = length_h * width_h
# print(ssquare_h_2)
# print(len.__doc__)
# print(help(len))
# def get_square(length, width):
#     return f' площадь равна: {length * width}'
# squer_2 = get_square(7, 5)
# squer_h = get_square(10,15)
# print(squer_2)
# print(squer_h)
# def get_square(length: int, width: int) -> int:
#     """Принимает длинну и ширину, возвращает площадь."""
#     return length*width
# print(help(get_square))

# word  = 'kyrgyzstan'
# def len1(iterable):
#     cougt = 0
#     for _ in iterable:
#         cougt += 1
#     return cougt
# print(len1(word))

list = [2,5,7,9]
list2 = [8,7,10,5]
def num(iterable):
    max = iterable[0]
    for max1 in iterable:
        print(max, max1)
        if max1 > max:
            max = max1
    return max

# print(num(list))
print(num(list2))

# def min1(iterable):
#     min = iterable[0]
#     for i in iterable[1:]:
#         if i < min:
#             min = i
#     return min

