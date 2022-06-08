#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # return [j for j in map(lambda x: x * number, my_list)]
    return list(map(lambda x: x * number, my_list))
