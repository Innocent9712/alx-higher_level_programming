#!/usr/bin/python3
"""
    module to save object in a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
