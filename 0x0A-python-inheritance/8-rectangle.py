#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module creates a class for task 8"""


class Rectangle(BaseGeometry):
    """
        Class Rectangle extends from  BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
