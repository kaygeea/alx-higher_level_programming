#!/usr/bin/python3
'''This module creates a func that performs a instance & inheritance check'''


def is_kind_of_class(obj, a_class):
    '''This func chcks if obj() is an inst or obj() of derived inst of a_class
    Args:
        obj: incoming arg for object to be checked.
        a_class: incoming arg for class against which obj() is to be checked.
    Return:
        True or False, depending on obj()'s type.
    '''

    return isinstance(obj, a_class)
