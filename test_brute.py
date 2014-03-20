"""Test suite."""


from unittest import TestCase

from brute import brute


class TestBrute(TestCase):

    def test_brute_length_default(self):
        last_str = ''
        for pw in brute():
            last_str = pw

        if len(last_str) != 3:
            return
