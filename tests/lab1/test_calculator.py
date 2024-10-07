import unittest
from src.lab1.calculator import calc

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    # def test_one(self):
    #     self.assertEqual(1, 1)

    def test_lab1(self):
        self.assertEqual(calc(10,20,"+"), 30)
        self.assertEqual(calc(20, 10, "-"), 10)
        self.assertEqual(calc(30, 10, "/"), 3)
        self.assertEqual(calc(50, 0, "/"), "На ноль делить нельзя!")


