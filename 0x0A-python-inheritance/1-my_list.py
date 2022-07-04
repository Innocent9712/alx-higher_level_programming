#!/usr/bin/python3
"""This module creates a class for task 1"""


class MyList(list):
    """
        This class extends from the list
        class and adds a sort method to it
    """
    def print_sorted(self):
        """
            Function to return a sorted list
        """
        print(sorted(self))
