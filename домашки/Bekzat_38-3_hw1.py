d1 = int(input("Расходы за понедельник:"))
d2 = int(input("Расходы за вторник:"))
d3 = int(input("Расходы за среду:"))
d4 = int(input("Расходы за четверг:"))
d5 = int(input("Расходы за пятницу:"))
d6 = int(input("Расходы за субботу:"))
d7 = int(input("Расходы за воскресенье:"))

total_expenses = d1 + d2 + d3 + d4 + d5 + d6 + d7
average_expense = round(total_expenses / 7, 1)

print("Расходы за неделю: " + str(total_expenses))
print("Средний расход в день: " + str(average_expense))


if average_expense >= 5000:
    print("потратили много")
elif average_expense >=1 and average_expense <= 500:
    print("потратили мало")
elif average_expense >= 501 and average_expense <= 4999:
    print("потратили средне")
else:
    print("потрачено ничего")
# если average_expense больще 10000 "потратили много"
# если меньше 500 "потратили мало"
# если от 501-4999 "потратили средне"
# иначе вывести "потрачено ничего"
#  """Управщённая версия домашки"""
# expenses = [int(input(f'введите расход ха день: {i}')) for i in range(1, 8)]
# print(sum(expenses) / len(expenses))