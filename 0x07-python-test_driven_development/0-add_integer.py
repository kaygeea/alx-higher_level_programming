#!/usr/bin/python3
'''This module builds a function that adds 2 integers, based on given specs'''


def add_integer(a, b=98):
    """This function adds 2 integers
    Args:
        a: must be of type int or float. If float, typecast to int first.
        b: must be of type int or float. If float, typecast to int first.
    Exceptions:
        TypeError: if neither a or b is an int or float.
    Return:
        Int: Sum of a and b
    """

    if ((isinstance(a, int) and isinstance(b, int))):
        sum = a + b
    elif ((isinstance(a, float) or isinstance(b, float))):
        sum = int(a) + int(b)
    else:
        if not (isinstance(a, int)) or (isinstance(a, float)):
            raise TypeError("a must be an integer")
        if not (isinstance(b, int)) or (isinstance(b, float)):
            raise TypeError("b must be an integer")
    return sum
