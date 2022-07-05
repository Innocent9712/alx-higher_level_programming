#!/usr/bin/python3
"""
    module to append to file
"""


def append_write(filename="", text=""):
    """
        function appends to the end of a text file
        and returns the number of characters added
    """
    with open(filename, mode='a', encoding="utf_8") as my_file:
        return my_file.write(text)
