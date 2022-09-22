#!/usr/bin/python3
'''
Module for task 6
'''


def find_peak(list_of_integers):
    '''
    Function to find the peak of a list of integers
    '''
    if list_of_integers == []:
        return None
    current_index = len(list_of_integers)//2
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
        next += 1

    while (prev >= 0):
        if (list_of_integers[prev] > peak):
            peak = list_of_integers[prev]
            return peak
        prev -= 1

    while (next < len(list_of_integers)):
        if (list_of_integers[next] > peak):
            peak = list_of_integers[next]
            return peak
        next += 1

    return peak
