#!/usr/bin/python3
"""This module creates a function for task 4"""


def inherits_from(obj, a_class):
    """
        Function to return True if an object is an instance
        of a specified class or inherited class, but not an instance of
        the a_class: otherwise False
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
