#!/usr/bin/python3
'''This module builds a class'''


class BaseGeometry(Exception):
    '''This class creates an exception
    Arg:
        Exception: expected arg of base class, to derive new exception class.
    '''

    pass

    def area(self):
        '''This method raises an exception'''

        raise Exception("area() is not implemented")
