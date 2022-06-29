#!/usr/bin/python3
"""
Function to print squares
"""


def print_square(size):
    """
        takes the size argument, makes sure that
        it is a valid integer and prints square with
        the area of the size
    """

    if type(size) is not int or \
            (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if not (size >= 0):
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
    # [print("#", end="") for x in range(size) for y in range(size)]
    # [print(print("#", end="") for x in range(size)) for x in range(size]
