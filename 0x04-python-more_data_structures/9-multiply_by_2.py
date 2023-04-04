#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''This func returns a new dictionary with all values multiplied by 2'''
    x2dict = {}
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            x2dict[key] = value * 2
        return x2dict
    return x2dict
