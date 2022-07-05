#!/usr/bin/python3
"""
    module to read object from a file
"""


import json


def load_from_json_file(filename):
    """
        function that reads an JSON string from  a text file,
        and returns it as a python object
    """
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)
