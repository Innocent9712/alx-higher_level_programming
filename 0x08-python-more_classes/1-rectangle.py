#!/usr/bin/python3

"""
    define a class Rectangle
"""


class Rectangle:
    """
        Initialze the rectangle class with width and
        height fields
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """
            Get the value of the width field
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Set the value of the width field
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the value of the height field
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Set the value of the height field
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
