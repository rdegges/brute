"""
    brute
    ~~~~~

    Simple brute forcing in Python.
"""


from itertools import chain, product
from random import sample

# Python 2 and 3 have different string constants, so this makes the library
# Python 3 compatible.
try:
    from string import (
        digits as _numbers,
        letters as _letters,
        punctuation as _symbols,
        whitespace as _spaces,
    )
except ImportError:
    from string import (
        digits as _numbers,
        ascii_letters as _letters,
        punctuation as _symbols,
        whitespace as _spaces,
    )


__version__ = '0.0.2'


def brute(length=3, ramp=True, letters=True, numbers=True, symbols=True, spaces=False):
    """
    Iterate through a sequence of possible strings, efficiently.

    :param int length: The length of the string to iterate through.  We'll
        iterate through all permutations of strings up to this length. Default:
        5.
    :param bool ramp: Should we ramp up in length from 1 until length?  Or
        should we only iterate over values of the current length?  Default:
        True.
    :param bool letters: Include letters (upper and lower case)? Default: True.
    :param bool numbers: Include numbers? Default: True.
    :param bool symbols: Include symbols? Default: True.
    :param bool spaces: Include space characters? Default: False.

    :rtype: generator
    :returns: A generator which iterates through all permutations of the
        specified values.
    """
    choices = ''
    choices += _letters if letters else ''
    choices += _numbers if numbers else ''
    choices += _symbols if symbols else ''
    choices += _spaces if spaces else ''
    choices = ''.join(sample(choices, len(choices)))

    return (
        ''.join(candidate) for candidate in
        chain.from_iterable(
            product(
                choices,
                repeat = i,
            ) for i in range(1 if ramp else length, length + 1),
        )
    )
