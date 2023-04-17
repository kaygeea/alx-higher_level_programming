#!/usr/bin/python3
'''This module creates a bool func that checks the "instanceness" of an obj'''


def is_same_class(obj, a_class):
    '''This func returns a bool based on if obj() is an instance of a_class
    Args:
        obj: incoming arg for object to be checked
        a_class: incoming arg for class against which obj() is to be checked
    Return:
        True or False, depending on if obj() is exactly an instance of a_class
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
