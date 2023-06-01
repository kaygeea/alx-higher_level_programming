#!/usr/bin/python3
'''Create and define a class - Rectangle.'''


class Rectangle:
    '''Define a rectangle() class'''

    def __init__(self, width=0, height=0):
        '''Define the object instantiation for rectangle()
        Args:
            width: incoming (optional) arg for width of a rectangle() object
            height: incoming (optional) arg for height of a rectangle() object
        '''

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get & set the width attribute of rectangle()"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width mustbe an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get & set the height attribute of a rectangle()"""
        return (self.__height)

    @height.setter
    def height(Self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle()"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of rectangle()"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """Print the rectangle with the '#' character"""
        if self.width == 0 or self.height == 0:
            return ("")

        rect = ""
        for column in range(self.height):
            for row in range(self.width):
                rect += "#"
            if column < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return an str rep of rectangle() that can be passed into eval()"""
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep
