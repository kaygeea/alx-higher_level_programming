#!/usr/bin/python3
'''This module builds a derived class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Derive from BaseGeometry base class to build a rectangle'''

    def __init__(self, width, height):
        '''Initialise the attributes of rectangle()
        Args:
            width: incoming argument for width of rectangle
            height: incoming argument for height of rectangle
        '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Return the area of rectangle()'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Print description of rectangle()'''
        rep = str(f"[{Rectangle.__name__}] {self.__width}/{self.__height}")
        return rep
