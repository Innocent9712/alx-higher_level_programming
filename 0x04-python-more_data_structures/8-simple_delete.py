#!/usr/bin/python3
from re import A


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    return a_dictionary
