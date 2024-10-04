import string
import unittest
import random
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    # def test_one(self):
    #     self.assertEqual(1, 1)

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))