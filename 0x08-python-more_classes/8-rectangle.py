#!/usr/bin/python3
'''Create and define a class - Rectangle.'''


class Rectangle:
    '''Define a rectangle() class'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Define the object instantiation for rectangle()
        Args:
            width: incoming (optional) arg for width of a rectangle() object
            height: incoming (optional) arg for height of a rectangle() object
        '''

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
    def height(self, value):
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
        """Print the rectangle with the character passed as 'print_symbol'"""
        if self.width == 0 or self.height == 0:
            return ("")

        rect = ""
        for column in range(self.height):
            for row in range(self.width):
                rect += str(self.print_symbol)
            if column < self.height - 1:
                rect += "\n"
        return rect

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area.
        Exceptions:
            a. TypeError: if rect_1 is not an instance of Rectangle()
            b. TypeError: if rect_2 is not an instance of Rectangle()
        Returns:
            a. rect_1 if the area of both rects are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        """Return an str rep of rectangle() that can be passed into eval()"""
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep

    def __del__(self):
        """Finalize the class during garbage collection"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
