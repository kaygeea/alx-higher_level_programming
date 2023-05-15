#!/usr/bin/python3
"""Create and define a sub-class - Rectangle()"""


class Rectangle(Base):
    """Inherit from Base class, create and define a rectangle() object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise rectangle() object
        Args:
            width (int): incoming argument for width of rectangle().
            height (int): incoming argument for height of rectangle().
            x (default = 0): incoming argument for the x axis of rectangle().
            y (default = 0): incoming argument for the y axis of rectangle().
            id (def = None): incoming argument for the id of rectangle().
        Exceptions:
            ValueError: if either of width or height is <=0.
            ValurError: if either x or y < 0
            TypeError: if either width or height is not type integer
            TypeError: if either x or y is not of type integer
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
