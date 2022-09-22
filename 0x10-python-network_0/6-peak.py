#!/usr/bin/python3
'''
Module for task 6
'''
import math


def find_peak(list_of_integers):
    '''
    Function to find the peak of a list of integers
    '''
    if len(list_of_integers) == 0:
        return None
    current_index = math.floor(len(list_of_integers)/2)
    peak = list_of_integers[current_index]
    prev = current_index - 1
    next = current_index + 1

    while (prev >= 0 and next <= len(list_of_integers) - 1):
        if (list_of_integers[prev] > peak):
            peak = list_of_integers[prev]
            return peak

        if (list_of_integers[next] > peak):
            peak = list_of_integers[next]
            return peak
        prev -= 1
        next -= 1
    return peak
