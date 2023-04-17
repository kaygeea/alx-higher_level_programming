#!/usr/bin/python3
'''This module builds a derived class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This class derives from BaseGeometry base class to build a rectangle'''

    def __init__(self, width, height):
        '''Initialises the attributes of rectangle()
        Args:
            width: incoming argument for width of rectangle
            height: incoming argument for height of rectangle
        '''

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
