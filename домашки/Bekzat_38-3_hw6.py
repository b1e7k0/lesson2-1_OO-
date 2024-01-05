movies = {
    "Django Unchained": {"John": 10, "Jack": 9},
    "Troy": {}
}

def get_movie_name(movie_name):
    return movies.get(movie_name)

def add_movie():
    movie_name = input("Введите название фильма: ").title()
    exist_movie = get_movie_name(movie_name)
    if exist_movie is None:
        movies[movie_name] = {}
        print("Фильм успешно был добавлен")
    else:
        print("Этот фильм уже существует")

def add_rating():
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
            print(f"Рейтинг был добавлен для фильма {movie_name}, {name} оценила его на {rating}")
        else:
            print('Рейтинг должен быть от 0 до 10')
    else:
        print("Этот фильм не существует")

def view_ratings():
    for movie_name, rating in movies.items():
        if rating:
            average_rating = sum(rating.values()) / len(rating)
            print(f"{movie_name} был оценён на {average_rating}")
        else:
            print(f"Пока рейтингов для {movie_name} нет")

while True:
    print(movies)
    command = input("1 - добавить фильм\n"
                    "2 - добавить рейтинг\n"
                    "3 - посмотреть рейтинги\n"
                    "4 - выход\n"
                    "Введите команду: ")

    if command == "1":
        add_movie()
    elif command == "2":
        add_rating()
    elif command == "3":
        view_ratings()
    elif command == "4":
        print("Выход")
        break
    else:
        print("Недоступная команда")