
while True:
    day = input("Введите день рождения: ")
    mounth = int(input("Введите месяц рождения: "))
    if day == 'stop':
        print("finish")
        break
    temp = int(temp)
    if day >= 21 and day <=31 and mounth == 3 or day >= 1 and day <= 20 and mounth == 4:
        print("Овен")
    elif day >= 21 and day <=30 and  mounth == 4 or day >= 1 and day <= 21 and mounth == 5:
        print("Телец")
    elif day >= 22 and day <=31 and mounth == 5 or day >= 1 and day <= 21 and mounth == 6:
        print("Близнецы")
    elif day >= 22 and day <=30 and mounth == 6 or day >= 1 and day <= 22 and mounth == 7:
        print("Рак")
    elif day >= 23 and day <=31 and mounth == 7 or day >= 1 and day <= 21 and mounth == 8:
        print("Лев")
    elif day >= 22 and day <=31 and mounth == 8 or day >= 1 and day <= 23 and mounth == 9:
        print("Дева")
    elif day >= 24 and day <=30 and mounth == 9 or day >= 1 and day <= 23 and mounth == 10:
        print("Весы")
    elif day >= 24 and day <=31 and mounth == 10 or day >= 1 and day <= 22 and mounth == 11:
        print("Скорпион")
    elif day >= 23 and day <=30 and mounth == 11 or day >= 1 and day <= 22 and mounth == 12:
        print("Стрелец")
    elif day >= 23 and day <=31 and mounth == 12 or day >= 1 and day <= 20 and mounth == 1:
        print("Козерог")
    elif day >= 21 and day <=31 and mounth == 1 or day >= 1 and day <= 19 and mounth == 2:
        print("Водолей")
    elif day >= 20 and day <=29 and mounth == 2 or day >= 1 and day <= 20 and mounth == 3:
        print("Рыбы")
    else:
        print("Пожалуйста, попробуйте занова, попробуйте написать месяц в числах")