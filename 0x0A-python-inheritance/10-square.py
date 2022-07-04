#!/usr/bin/python3
"""This module creates a class for task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Class Square extends from  Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        # super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
