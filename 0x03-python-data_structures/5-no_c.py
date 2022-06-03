#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c in 'cC':
            index = my_string.index(c)
            my_string = my_string[:index] + my_string[index + 1:]
    return my_string
