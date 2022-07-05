#!/usr/bin/python3
"""Module for class Student"""


class Student():
    """class Student thst defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        return {attr: self.__dict__[attr] for attr in attrs
                if attr in self.__dict__}

        # result_dict = {}
        # for attr in attrs:
        #     if attr in self.__dict__:
        #         result_dict[attr] = self.__dict__[attr]
        # return result_dict
