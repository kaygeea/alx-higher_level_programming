#!/usr/bin/python3
'''A module that creates a class and defines it accordingly'''


class Square:
    '''A class that defines and initialises a sqaure'''

    def __init__(self, size=0):
        '''Initialises square() objects
        Args:
            size: represenets the size of the square() object
        Exceptions:
            TypeError: if size passed is not integer
            ValueError: if size passed is less than zero
        '''

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''returns the area of square()'''
        
        return (self.__size * self.__size)
