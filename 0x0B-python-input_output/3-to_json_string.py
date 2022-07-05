#!/usr/bin/python3
"""
    module to convert python object to JSON
"""


import json


def to_json_string(my_obj):
    """
        function converts python object to JSON
    """
    return(json.dumps(my_obj))
