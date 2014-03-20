"""Test suite."""


from types import GeneratorType
from unittest import TestCase

from brute import brute


class TestBrute(TestCase):

    def test_brute_length_default(self):
        last_str = ''
        for pw in brute():
            last_str = pw

        self.assertEqual(len(last_str), 3)

    def test_brute_returns_generator(self):
        self.assertIsInstance(brute(), GeneratorType)

    def test_letters_numbers_symbols_whitespace_default(self):
        letters = False
        numbers = False
        symbols = False
        whitespace = True

        for pw in brute():
            if 'a' in pw:
                letters = True
            elif '1' in pw:
                numbers = True
            elif '!' in pw:
                symbols = True
            elif ' ' in pw:
                whitespace = False

        self.assertTrue(letters)
        self.assertTrue(numbers)
        self.assertTrue(symbols)
        self.assertTrue(whitespace)
