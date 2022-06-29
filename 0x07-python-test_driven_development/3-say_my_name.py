#!/usr/bin/python3
"""
Function to print full name

"""


def say_my_name(first_name, last_name=""):
    """
        takes first_name and last name,
        checks that they are valid strings
        and prints to output
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
