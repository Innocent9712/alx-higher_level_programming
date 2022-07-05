#!/usr/bin/python3
"""
    module to write to file
"""


def write_file(filename="", text=""):
    """
        function receives a filename and a text
        then writes the text into the file with the file name
        returning the number of characters written
    """
    with open(filename, mode='w', encoding="utf_8") as my_file:
        return my_file.write(text)
