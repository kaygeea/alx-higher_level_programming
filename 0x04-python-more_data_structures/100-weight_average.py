#!/usr/bin/python3
'''This module builds a function that returns weighted average'''


def weight_average(my_list=[]):
    '''This function returns the weighted average of all integers tuple'''

    if not my_list:
        return 0
    val_weight = sum([int(vals[0]) * int(vals[1]) for vals in my_list])
    weight = sum([int(w[1]) for w in my_list])
    return val_weight / weight
