#!/usr/bin/python3
"""Module for class Student"""


class Student():
    """class Student thst defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # @property
    # def first_name(self):
    #     return self.__first_name

    # @first_name.setter
    # def first_name(self, value):
    #     self.__first_name = value

    # @property
    # def last_name(self):
    #     return self.__last_name

    # @last_name.setter
    # def last_name(self, value):
    #     self.__last_name = value

    # @property
    # def age(self):
    #     return self.__age

    # @age.setter
    # def age(self, value):
    #     self.__age = value

    def to_json(self):
        return self.__dict__
