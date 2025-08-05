import random

# Создание списка городов из файла cities.txt
f = open("cities.txt", encoding="utf-8")
cities_list = [line.strip().lower() for line in f]
f.close()


# Функция для определения последней буквы города
def get_last_char(city):
    last_char = city[-1]
    if last_char in "ьъый":
        last_char = city[-2]
        if last_char in "ьъый":
            last_char = city[-3]
    return last_char


def game():
    current_city = random.choice(cities_list)  # начальный город
    print(
        f"Первый город: {current_city}. Подбери слово на букву: {get_last_char(current_city)}"
    )
    with open(
        "answers.txt", "w", encoding="utf-8"
    ) as f:  # открываем файл answers.txt для записи ответов
        f.write(f"{current_city}\n")
    last_char = get_last_char(current_city)  # определение последней буквы
    used_cities = []  # список для сохранения использованных городов
    attempts = 5  # количество попыток для игрока
    while attempts > 0:
        user_city = input(f"Введите город: ").lower()
        fa = open("answers.txt", encoding="utf-8")
        answer_list = [line.strip().lower() for line in fa]
        if (
            user_city in cities_list
        ):  # проверка слова игрока на наличие в списке городов
            if (
                get_last_char(current_city) == user_city[0]
            ):  # проверка слова игрока на соответствие
                used_cities.append(current_city)
                if (
                    user_city not in used_cities
                ):  # проверка на повторяемость слов игрока
                    used_cities.append(user_city)
                    for city in cities_list:
                        if (
                            get_last_char(user_city) == city[0]
                            and city not in used_cities
                        ):  # проверка на повторяемость и поиск подходящего слова для компьютера
                            with open("answers.txt", "a", encoding="utf-8") as f:
                                f.write(f"{current_city}\n")
                                f.write(f"{user_city}\n")
                            print(
                                f"Ход компьютера: {city}. Подбери слово на букву : {get_last_char(city)}"
                            )
                            current_city = city
                            break
                else:
                    attempts -= 1
                    print(
                        f"Это слово уже использовалось ранее! Попыток осталось: {attempts}"
                    )
            else:
                attempts -= 1
                print(
                    f"Город начинается не на правильную букву. Осталось попыток: {attempts}"
                )
        else:
            attempts -= 1
            print(f"Города нет в списке городов. Осталось попыток: {attempts}")
        if attempts == 0:
            print("Попытки закончились. Компьютер выиграл!")
            break
        elif get_last_char(user_city) != city[0] and all(
            city in used_cities for city in cities_list
        ):
            print("Компьютер проиграл!")
            break


game()
