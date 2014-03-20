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
