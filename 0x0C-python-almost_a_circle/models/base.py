#!/usr/bin/python3
"""
    Module for Base Class
"""


import json
import os.path


class Base():
    """
        Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initializing an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            converts a list of dictionaries to a list
            of objects as json string
        """
        if list_dictionaries == "" or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            converts a json string of a list to a python
            list of dictionaries
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Saves a list of objects as json string
            to a file of class name
        """
        file_name = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for j in list_objs:
                my_list.append(cls.to_dictionary(j))
        with open(file_name, mode='w', encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """
            Creates an instance of a class from
            a dictionary of class data
        """
        if cls.__name__ == "Rectangle":
            placeholder = cls(1, 1)
        elif cls.__name__ == "Square":
            placeholder = cls(1)
        placeholder.update(**dictionary)
        return placeholder

    @classmethod
    def load_from_file(cls):
        """
            Gets json string from file of class name,
            String is decoded to a list of dictionaries in python.
            Each dictionary is used to create an instance of the class
            a list of instances is returned
        """
        file_name = cls.__name__ + ".json"
        my_list = []
        if(os.path.exists(file_name)):
            with open(file_name, 'r') as my_file:
                my_list = cls.from_json_string(my_file.read())
            for i, item in enumerate(my_list):
                my_list[i] = cls.create(**my_list[i])
        return my_list
