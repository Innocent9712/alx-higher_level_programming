#!/usr/bin/python3
"""This module creates a function for task 2"""


def is_same_class(obj, a_class):
    """
        Function to return True if an object is exactly an instance
        of a specified class: otherwise False
    """

    return type(obj) is a_class
