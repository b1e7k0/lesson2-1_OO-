
mentors = ['Кубаныч', 'Мирлан' ,'Гулина' ,'Камилия']

print('Добавление, Изменение, Удаление, Выход')
while True:
    a =  input('Выберите действие: ').title()
    if a == "Добавление":
        mentor = input('Введите имя ментора: ').title()
        if len(mentor) < 15 and mentor not in mentors:
            mentors.append(mentor)
        else:
            print("Введенно неправильно!")
    elif a == "Изменение":
         addmentor = input('Какое имя заменить: ').title()
         if addmentor in mentors:
            appmentor = input('На какое имя заменить: ').title()
            if len(appmentor) < 15 and appmentor not in mentors:
                i = mentors.index(addmentor)
                mentors[i] = appmentor
            else:
                print("Введенно неправильно!")    
         else:
            print('Такого имени нет в списке!')
    elif a == "Удаление":
         add = input('Удалить "по индексу" или "по имени": ')
         if add == "по индексу":
             index = int(input('Введите индекс ментора: '))
             if index <= len(mentors) and index > 0:
                 mentors.pop(index - 1)
             else:
                 print("Введён неправильный индекс!")
         elif add == "по имени":
             name = input('Введите имя: ').title()
             if name in mentors:
                 mentors.remove(name)
             else:
                 print("Введено неправильное имя!")
         else:
             print("Введенно некорректно!")
    elif a == "Выход":
        break
    else:
        print("Введенно неправильное действие!")
    print(mentors)
print(tuple(mentors))