#!/usr/bin/python
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

    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            if (text[i + 1] == ' '):
                i += 2
                continue
            i += 1
            continue
        print(text[i], end="")
        i += 1
