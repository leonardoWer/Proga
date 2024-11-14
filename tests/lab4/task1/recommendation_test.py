import unittest
from src.lab4.task1 import numbers_to_films, SokolUser


class FilmRecommendationTestCase(unittest.TestCase):

    def test_numbers_to_films(self):
        # given
        films_list = [["1", "Хатико"], ["2", "Мстители"]]
        numbers_list = ["2", "2"]

        # when
        result = numbers_to_films(films_list, numbers_list)

        # then
        self.assertEqual(result, ['Мстители', 'Мстители'])

    def test_find_recommendation(self):
        # given
        user = SokolUser(2, 4)

        # when
        user.get_history()
        recommendation = user.select_film_recommendation()

        # then
        self.assertEqual(recommendation, 'Дюна')


if __name__ == '__main__':
    unittest.main()
