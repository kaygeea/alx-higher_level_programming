#!/usr/bin/python3
'''The module creates and defines a class - Rectangle.'''


class Rectangle:
    '''This class defines a rectangle() class'''

    def __init__(self, width=0, height=0):
        '''This method defines the object instantiation for rectangle()
        Args:
            width: incoming (optional) arg for width of a rectangle() object
            height: incoming (optional) arg for height of a rectangle() object
        '''

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Gets and sets the width of a rectangle() object'''

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets and sets the height of a rectangle() object'''

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
