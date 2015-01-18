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

    def test_disable_letters(self):
        letters = True

        for pw in brute(letters=False):
            if 'a' in pw:
                letters = False

        self.assertTrue(letters)

    def test_disable_numbers(self):
        numbers = True

        for pw in brute(numbers=False):
            if '1' in pw:
                numbers = False

        self.assertTrue(numbers)

    def test_disable_symbols(self):
        symbols = True

        for pw in brute(symbols=False):
            if '!' in pw:
                symbols = False

        self.assertTrue(symbols)

    def test_enable_spaces(self):
        spaces = False

        for pw in brute(spaces=True):
            if ' ' in pw:
                spaces = True

        self.assertTrue(spaces)

    def test_ramp(self):
        for pw in brute(length=3, ramp=False):
            self.assertEqual(len(pw), 3)
