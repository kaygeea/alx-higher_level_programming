#!/usr/bin/python3
'''This module creates a bool func that checks the "instanceness" of an obj'''


def is_same_class(obj, a_class):
    '''This func returns a bool based on if obj is an instance of a_class'''

    if isinstance(obj, a_class):
        return True
    elif not isinstance(obj, a_class):
        return False
