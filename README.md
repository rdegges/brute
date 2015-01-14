# brute

[![PyPI version](https://badge.fury.io/py/brute.png)](http://badge.fury.io/py/brute)
[![Build Status](https://travis-ci.org/rdegges/brute.svg?branch=develop)](https://travis-ci.org/rdegges/brute)
[![Downloads](https://pypip.in/d/brute/badge.png)](https://pypi.python.org/pypi/brute/)

Simple brute forcing in Python.


![Devil Sketch](https://github.com/rdegges/brute/raw/master/assets/devil-sketch.jpg)


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

0.0.2: not yet released

    - Fixed typo in docstring.  Thanks @zhao-ji!


0.0.1: 3-20-2014

    - First release!
