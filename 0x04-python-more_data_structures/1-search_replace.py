#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''return [my_list[x] = replace if my_list[x] == search else my_list[x]
    for x in range(len(my_list))]'''
    new_list = my_list[:]
    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
