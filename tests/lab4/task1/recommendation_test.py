import unittest
from src.lab4.task1 import numbers_to_films, SokolUser


class FilmRecommendationTestCase(unittest.TestCase):

    def test_numbers_to_films(self):
        # given
        films_list = [["1", "Хатико"], ["2", "Мстители"]]
        numbers_list = ["2", "2"]
        films_list1 = [["1", "Хатико"], ["2", "Мстители"]]
        numbers_list1 = ["1", "1"]
        films_list2 = [["1", "Хатико"], ["2", "Мстители"]]
        numbers_list2 = ["1", "2"]

        # when
        result = numbers_to_films(films_list, numbers_list)
        result1 = numbers_to_films(films_list1, numbers_list1)
        result2 = numbers_to_films(films_list2, numbers_list2)

        # then
        self.assertEqual(result, ['Мстители', 'Мстители'])
        self.assertEqual(result1, ['Хатико', 'Хатико'])
        self.assertEqual(result2, ['Хатико', 'Мстители'])

    def test_find_recommendation(self):
        # given
        user = SokolUser(2, 4)
        user1 = SokolUser(1)
        user2 = SokolUser(1,2,3)

        # when
        user.get_history() # Проверяем, что выведенное соответствует информации в файле

        recommendation = user.select_film_recommendation()
        recommendation1 = user1.select_film_recommendation()
        recommendation2 = user2.select_film_recommendation()

        # then
        self.assertEqual(recommendation, 'Дюна')
        self.assertEqual(recommendation1, 'Хатико')
        self.assertEqual(recommendation2, 'Для подбора рекомендации не хватает данных')


if __name__ == '__main__':
    unittest.main()
