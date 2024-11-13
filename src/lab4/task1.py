"""Алгоритм рекомендации просмотра фильмов"""


def numbers_to_films(films_list:list, numbers_list:list) -> list:
    """
    Сопоставляет названия фильмов и их номера
    >>> numbers_to_films([["1", "Хатико"], ["2", "Мстители"]], ["2", "2"])
    ['Мстители', 'Мстители']
    """
    numbers_to_films_list = []
    for number in numbers_list:
        for film in films_list:
            if film[0] == number:
                numbers_to_films_list.append(film[1])
    return numbers_to_films_list


def get_films_list() -> list:
    """Считывает все фильмы из файла films"""
    films_list = []
    with open("task1-input/films.txt", "r", encoding="utf-8") as films:
        for film in films:
            films_list.append(list(map(str, film.strip().split(","))))

    return films_list


def films_history() -> list:
    """
    Обрабатывает историю пользователей:
     - Возвращает список, в котором история пользователей(номера) соответствуют названию фильмов
    """
    history = []
    with open("task1-input/history.txt", "r", encoding='utf8') as users_history:
        for user_history in users_history:
            history.append(list(user_history.strip().split(",")))

    films_list = get_films_list()

    other_users_history = []
    for user_history in history:
        user_numbers_to_films = numbers_to_films(films_list, user_history)
        other_users_history.append(user_numbers_to_films)

    return other_users_history


class Recommendation:
    other_users_history = []
    user_history = []
    films_list = get_films_list()

    def __init__(self, *user_history):
        self.other_users_history = films_history()
        self.user_history = numbers_to_films(self.films_list, list(str(user_history)))

    def get_user_history(self):
        print(self.user_history)

    def cnt_views(self, correct_films_list: list):
        cnt_views_accepted_films = []
        cnt_views = 0
        for film in correct_films_list:
            for other_user_films in self.other_users_history:
                for other_film in other_user_films:
                    if film == other_film:
                        cnt_views += 1
            cnt_views_accepted_films.append(cnt_views)

        return cnt_views_accepted_films

    def film_recommendation(self):
        accepted_films = []
        for film in self.user_history:
            for other_user_history in self.other_users_history:
                cnt_correct_films = 0
                for film_name in set(other_user_history):
                    if film_name == film:
                        cnt_correct_films += 1

                if cnt_correct_films >= len(self.user_history):
                    accepted_films.append(set(other_user_history + self.user_history) )

        cnt_views_correct_films = self.cnt_views(accepted_films)
        return max(cnt_views_correct_films)


if __name__=="__main__":
    person_recommendation = Recommendation(2, 4)
    person_recommendation.get_user_history()
    person_recommendation.film_recommendation()

