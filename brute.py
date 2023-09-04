"""Simple brute forcing in Python."""


from itertools import chain, product
from random import sample
from string import ascii_letters, digits, punctuation, whitespace


def brute(start_length=1, length=3, ramp=True, letters=True, numbers=True, symbols=True, spaces=False):
    """
    Iterate through a sequence of possible strings, efficiently.

    :param int start_length: The length of the string to begin ramping through.
        This number must be less than length and greater than 0. Default: 1.
    :param int length: The length of the string to iterate through.  We'll
        iterate through all permutations of strings up to this length. Default: 3.
    :param bool ramp: Should we ramp up in length from 1 until length?  Or
        should we only iterate over values of the current length?  Default: True.
    :param bool letters: Include letters (upper and lower case)? Default: True.
    :param bool numbers: Include numbers? Default: True.
    :param bool symbols: Include symbols? Default: True.
    :param bool spaces: Include space characters? Default: False.

    :rtype: generator
    :returns: A generator which iterates through all permutations of the specified values.
    """
    choices = ''
    choices += ascii_letters if letters else ''
    choices += digits if numbers else ''
    choices += punctuation if symbols else ''
    choices += whitespace if spaces else ''
    choices = ''.join(sample(choices, len(choices)))

    if ramp:
        if start_length < 1 or start_length > length:
            start_length = 1

    return (
        ''.join(candidate) for candidate in
        chain.from_iterable((product(choices, repeat=i) for i in range(start_length if ramp else length, length+1)))
    )
