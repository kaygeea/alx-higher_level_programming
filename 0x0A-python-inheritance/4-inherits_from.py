#!/usr/bin/python3
'''This module creates a function that performs a derived instance check'''


def inherits_from(obj, a_class):
    '''This function checks if obj() is a derived instance of a_class
    Args:
        obj: incoming arg for object to be checked.
        a_class: incoming arg for class against which obj() is to be checked.
    Return:
        True or False, depending on obj()'s type.
    '''

    if type(obj) != a_class and if issubclass(type(obj), a_class:
        retturn True
    return False
