import unittest
import random
import string
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CaesarTestCase(unittest.TestCase):

    def test_caesar(self):
        self.assertEqual(encrypt_caesar("PPPppp"), "SSSsss")
        self.assertEqual(decrypt_caesar("SSSsss"), "PPPppp")
        self.assertEqual(encrypt_caesar("12345"), "12345")