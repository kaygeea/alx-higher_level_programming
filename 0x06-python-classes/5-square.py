#!/usr/bin/python3
"""A module that creates a class and defines it accordingly"""


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
        self.size = size

    @property
    def size(self):
        """Gets/sets the size of square() object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of square() object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square() with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
