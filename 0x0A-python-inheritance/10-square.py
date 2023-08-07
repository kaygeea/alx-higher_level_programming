#!/usr/bin/python3
"""Build a class that inherits from another"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Derive from Rectangle class to build a square()"""
    def __init__(self, size):
        """Instantiate square() object"""
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Return the area of square()"""
        return (self.__size * self.__size)

    def __str__(self):
        """Return string representation of square()"""
        str_rep = str(f"[{Square.__bases__[0].__name__}] "
                      f"{self.__size}/{self.__size}")
        return str_rep
