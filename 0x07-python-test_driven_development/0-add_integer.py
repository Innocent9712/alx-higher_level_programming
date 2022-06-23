#!/usr/bin/python
"""
Function to add two integers
returns the sum of arguments
a and b, while making sure both
"""


def add_integer(a, b=98):
    """
        arguments are used as type of int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
