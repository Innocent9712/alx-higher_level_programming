#!/usr/bin/python3
"""
    module to convert  JSON string to python object
"""


import json


def from_json_string(my_str):
    """
        function converts JSON to python object
    """
    return(json.loads(my_str))
