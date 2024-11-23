"""
Содержит:
1. Алгоритм рекомендации фильмов для пользователя на основе его истории просмотра фильмов
2. Функцию считывания фильмов из файла
3. Функцию считывания истории пользователей из файла
4. Функцию перевода истории пользователей в номерах фильмов в историю пользователя в названиях фильмов
"""

import os


class InputInfo:
    """Класс, который обрабатывает информацию из файлов"""

    def numbers_to_films(self, films_list: list, numbers_list: list) -> list:
        """
        Сопоставляет названия фильмов и их номера
        >>> self.numbers_to_films([["1", "Хатико"], ["2", "Мстители"]], ["2", "2"])
        ['Мстители', 'Мстители']
        """
        numbers_to_films_list = []
        for number in numbers_list:
            for film in films_list:
                if film[0] == number:
                    numbers_to_films_list.append(film[1])
        return numbers_to_films_list

    def get_films_list(self) -> list:
        """Считывает все фильмы из файла films"""
        films_list = []
        current_dir = os.path.dirname(os.path.abspath(__file__)) # Путь до текущей папки
        relative_path = "task1-input/films.txt" # Относительный путь
        absolute_path = os.path.join(current_dir, relative_path) # Абсолютный путь до папки с файлом

        with open(absolute_path, "r", encoding="utf-8") as films:
            for film in films:
                films_list.append(list(map(str, film.strip().split(","))))

        return films_list

    def films_history(self) -> list:
        """
        Обрабатывает историю пользователей:
         - Возвращает список, в котором история пользователей(номера) сопоставлены с фильмами
         - Пример: (2,2) -> ([Хатико, 2], [Хатико, 2])
        """
        history = []
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Путь до текущей папки
        relative_path = "task1-input/history.txt"  # Относительный путь
        absolute_path = os.path.join(current_dir, relative_path)  # Абсолютный путь до папки с файлом

        with open(absolute_path, "r", encoding='utf8') as users_history:
            for user_history in users_history:
                history.append(list(user_history.strip().split(",")))

        films_list = self.get_films_list()

        other_users_history = []
        for user_history in history:
            user_numbers_to_films = self.numbers_to_films(films_list, user_history) # Переводим номера в названия
            other_users_history.append(user_numbers_to_films)

        return other_users_history


class SokolUser:
    """Класс характеризующий пользователя кинотеатра Сокол"""
    user_history = []
    other_users_history = []
    films_list = []

    def __init__(self, *user_history):
        utils = InputInfo()
        self.other_users_history = utils.films_history()
        self.films_list = utils.get_films_list()
        self.user_history = utils.numbers_to_films(self.films_list, list(str(user_history)))

    def get_history(self):
        """ Выводит историю пользователя и историю всех пользователей"""
        print(f"История текущего пользователя: {self.user_history}")
        print(f"История всех пользователей: {self.other_users_history}")

    def cnt_views(self, correct_films_list: list):
        """
        Подсчитывает количество просмотров фильмов среди всех пользователей
         - Принимает: список с фильмами
         - Возвращает: список с просмотрами этих фильмов
        """
        cnt_views_accepted_films = [] # Список сот списками в которых: [количество просмотров, фильм]
        for film in correct_films_list:
            cnt_views = 0
            for other_user_films in self.other_users_history:
                for other_film in other_user_films:
                    if film == other_film:
                        cnt_views += 1
            cnt_views_accepted_films.append([cnt_views, film])

        return cnt_views_accepted_films

    def select_film_recommendation(self):
        """ Подбирает рекомендацию для пользователя """
        accepted_films = [] # Список рекомендаций для пользователя
        for film in self.user_history:
            for other_user_history in self.other_users_history:
                cnt_correct_films = 0
                for film_name in other_user_history:
                    if film_name == film:
                        cnt_correct_films += 1
                if cnt_correct_films >= len(self.user_history):
                    accepted_films += ([film for film in other_user_history if film not in self.user_history])

        cnt_views_correct_films = self.cnt_views(accepted_films)
        try:
            user_recommendation = max(cnt_views_correct_films)[-1]
            return user_recommendation
        except ValueError:
            return "Для подбора рекомендации не хватает данных"

    def get_user_recommendation(self):
        print(f"Мы рекомендуем вам посмотреть фильм {self.select_film_recommendation()}!")


if __name__ == "__main__":
    user = SokolUser(2, 4)
    user.get_user_recommendation()
