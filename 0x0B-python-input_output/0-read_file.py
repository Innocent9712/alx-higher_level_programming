#!/usr/bin/python3
"""
    module to read a file and print to stdout
"""


def read_file(filename=""):
    """
        function accepts a filename and attempts to
        read from the file
    """
    with open(filename, encoding="utf_8") as my_file:
        print(my_file.read(), end="")
