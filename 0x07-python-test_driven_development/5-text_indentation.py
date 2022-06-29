#!/usr/bin/python3
"""
Function to break a text with two new lines at
certain charractera
"""


def text_indentation(text):
    """
    checks that text argument is valid string
    then implement logic to perform spiting
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    for a in text:
        if i == 0:
            if a == ' ':
                continue
            else:
                i = 1
        if i == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                i = 0
            else:
                print(a, end="")
