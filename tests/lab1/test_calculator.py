import unittest
from src.lab1.calculator import main

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_one(self):
        self.assertEquals(1, 1)

    def test_lab1(self):
        self.assertEquals(main(10,20,30))

    