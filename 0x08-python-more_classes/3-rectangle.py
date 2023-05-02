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

        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets and sets the width of a rectangle() object'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets and sets the height of a rectangle() object'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''This method returns the area of a rectangle() object'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''This method returns the perimeter of a rectangle() object'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        '''Prints a visual representation of a rectangle() object,
            representing the rectangle() object with the '#' character
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        vizRect = []
        for i in range(self.__height):
            [vizRect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                vizRect.append("\n")
        return ("".join(vizRect))
