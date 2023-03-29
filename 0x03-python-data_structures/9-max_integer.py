#!/usr/bin/python3

def max_integer(my_list=[]):
    '''This function finds the biggest integer of a list'''

    if len(my_list) == 0:
        return "None"

    tmp_max = my_list[0]

    for x in my_list:
        if x > tmp_max:
            tmp_max = x

    return tmp_max
