#!/usr/bin/python3
"""This module creates a class for task 5"""


class BaseGeometry():
    """
        Class BaseGeometry
    """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validate that value is an integer and
            greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
