#!/usr/bin/python3
'''This module builds a function that converts a class to JSON'''


def class_to_json(obj):
    '''This function returns the dict representation of a simple data stuct.
    Arg:
        obj: incoming argument for object whose dict rep is to be returned.
    '''

    return obj.__dict__
