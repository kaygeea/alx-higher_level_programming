#!/usr/bin/python3
'''Creates a class and defines it accordingly'''


class Square:
    '''Defines and instantiates the class Square'''

    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
