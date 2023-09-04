# brute

[![PyPI Version](https://img.shields.io/pypi/v/brute.svg)](https://pypi.python.org/pypi/brute)
[![PyPI Downloads](https://img.shields.io/pypi/dm/brute.svg)](https://pypi.python.org/pypi/brute)
[![Travis Build Status](https://img.shields.io/travis/rdegges/brute.svg)](https://travis-ci.org/rdegges/brute)

Simple brute forcing in Python.

## Purpose

Brute forcing passwords, and other things often requires a bit of hacking to get
working properly.

This library makes generating all possible permutations of strings really easy
-- and is very customizable.

You can then brute force whatever you want, however you want &gt;:)


## Installation

Installing `brute` is easy with [pip](http://pip.readthedocs.org/en/latest/).
Just go to the terminal and run:

```console
$ pip install brute
```

You can also upgrade your existing installation by running:

```console
$ pip install -U brute
```


## Usage

Using `brute` is super easy -- seriously.

Let's say you want to iterate through every possible permutation of strings that
contain:

- All letters (upper and lowercase),
- All numbers (01234...),
- All symbols (!#$...),

All you have to do is:

```python
from brute import brute

for s in brute():
    print s
```

Bam!

Let's say you want to also include space characters in your string (`' '`,
`'\t'`, etc...) -- you can do this too!

```python
from brute import brute

for s in brute(spaces=True):
    print s
```

You can customize the max length of the strings generated as well.  By
default, `brute` will only run through 3 characters:

```
from brute import brute

for s in brute(length=10)
    print s
```

And, lastly, if for some reason you only want to iterate through letters,
numbers, or whatever, you can do that as well!

```python
from brute import brute

# Iterate over *only* numbers (0 - 9).
for s in brute(length=5, letters=False, numbers=True, symbols=False):
    print s
```


## Changes

0.0.4: 8-8-2023

    - Fix syntax error (issues rdegges#7, rdegges#12, rdegges#14)

0.0.3: 2-12-2016

    - Supporting start length when ramping up. Thanks @petermuller!

0.0.2: 1-18-2015

    - Fixed typo in docstring.  Thanks @zhao-ji!


0.0.1: 3-20-2014

    - First release!
