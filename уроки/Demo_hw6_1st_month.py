
# movie = []
# user_names = []
# ratings =[]
# def films(movie:str, user_names:str, ratings="Rating is not yet available for movie_name") -> dict:

#     while True:

#         print('Добавить фильм/ Добавить рейтинг к фильму/ Посмотреть рейтинг фильма/ Выход ') 
#         action = str(input("Введите действие: ")).title()
#         movie_name = input("Введите название фильма: ").title()
#         movie = movie_name
#         index = 0
#         print(action)     
#         if action == "Добавить фильм":
#             print(movie).title()
#             if movie not in films:
#                 movie.append(action)
#                 print("Movie added successfully")
#             else:
#                 print("This movie already exist!")
#         elif action == "Добавить рейтинг к фильму":
#             print(movie).title()
#             if movie not in films:
#                 print("This movie doesn't exist")
#             elif movie in films:
#                 user_name = input("Введите ваше имя: ").title()
#                 if user_name not in user_names:
#                     user_names.append(user_name)
#                 else:
#                     print("Введите дургое имя!")
#                 rating = int(input("Введите оценку: "))
#                 if 0 <= rating <= 10:
#                     ratings.append(rating)
#                     movie_rating = dict(zip(user_names, ratings))
#                 else:
#                     print("Не соответствующая оценка!")
#             print(f'A rating has been added for {movie}: {user_name} rated it {rating}')
#         elif action == "Посмотреть рейтинг фильма":
#             avarage_rating = sum(ratings) / len(user_names) if len(user_names) > 0 else "Rating is not yet available for movie_name"
#             print(f'{movie} is rated: {avarage_rating: .2f}')

#         elif action == "Выход":
#             break
#         else:
#             print("Введено неверное действие!")
#         return dict(zip(movie, movie_rating))


#     films()


# movies = {
#     "Django Unchained": {
#         "John": 10,
#         "Jack": 9
#     },
#     "Troy": {}
# }
# def manage_movies():
#     while True:
#         print('Добавить фильм/\n '
#               'Добавить рейтинг к фильму/\n'
#               'Посмотреть рейтинг фильма/\n'
#               'Выход ')
#         action = input("Введите действие: ").title()
#
#         if action == "Добавить фильм":
#             movie_name = input("Введите название фильма: ").title()
#             if movie_name not in movies_list:
#                 movies_list.append(movie_name)
#                 print("Фильм успешно добавлен")
#             else:
#                 print("Этот фильм уже существует!")
#
#         elif action == "Добавить рейтинг к фильму":
#             movie_name = input("Введите название фильма: ").title()
#             if movie_name not in movies_list:
#                 print("Этот фильм не существует")
#             else:
#                 user_name = input("Введите ваше имя: ").title()
#                 if user_name not in user_names:
#                     user_names.append(user_name)
#                 else:
#                     print("Введите другое имя!")
#                 rating = float(input("Введите оценку: "))
#                 if 0 <= rating <= 10:
#                     ratings.append(rating)
#                     movie_rating = dict(zip(user_names, ratings))
#                     print(f'Рейтинг добавлен для {movie_name}: {user_name} оценил на {rating}')
#                 else:
#                     print("Некорректная оценка!")
#
#         elif action == "Посмотреть рейтинг фильма":
#             movie_name = input("Введите название фильма: ").title()
#             if movie_name not in movies_list:
#                 print("Этот фильм не существует")
#             else:
#                 average_rating = sum(ratings) / len(user_names) if len(user_names) > 0 else 0
#                 print(f'Средний рейтинг для {movie_name}: {average_rating:.2f}')
#
#         elif action == "Выход":
#             break
#
#         else:
#             print("Введено неверное действие!")
#
# manage_movies()


movies = {
    "Django Unchained": {"John": 10, "Jack": 9},
    "Troy": {}
}


def get_movie_name(movie_name):
    return movies.get(movie_name)


while True:
    print(movies)
    command = input("1 - добавить фильм\n"
                    "2 - добавить рейтинг\n"
                    "3 - посмотреть рейнтинги\n"
                    "4 - выход\n"
                    "Введите команду: ")
    if command == "1":
        movie_name = input("Введите название фильма: ").title()
        exist_movie = get_movie_name(movie_name)
        if exist_movie is None:
            movies[movie_name] = {}
            print("Фильм успешно был добавлен")
        else:
            print("Этот фильм уже существует")
    elif command == "2":
        movie_name = input("Введите название фильма: ").title()
        exist_movie = get_movie_name(movie_name)
        if exist_movie is not None:
            rating = int(input("Введите рейтинг: "))
            if 0 <= rating <= 10:
                name = input("Введите ваше имя: ").title()
                while name in exist_movie:
                    print("Введите другое имя")
                    name = input("Введите ваше имя: ").title()
                exist_movie[name] = rating
                print(f"Рейтинг был добавлен для фильма {movie_name}, {name} Оценила его на {rating}")
            else:
                print('Рейтинг должен быть от 0 до 10')
        else:
            print("Этот фильм не существует")
    elif command == "3":
        for movie_name, rating in movies.items():
            if rating:
                average_rating = sum(rating.values()) / len(rating)
                print(f"{movie_name} был оценён на {average_rating}")
            else:
                print(f"пока рейтингов для {movie_name} нет")
    elif command == "4":
        print("Выход")
        break
    else:
        print("Недоступная команда")
