#!/usr/bin/python3
'''This module builds a class'''


class BaseGeometry:
    '''This class creates a class BaseGeometry'''

    pass

    def area(self):
        '''This non-implemented method raises an Exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''This method validates incoming arg - value
        Args:
            name: incoming arg for name of item to which value is assigned
            value: incoming arg for value of name
        Exceptions:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        '''
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if isinstance(value, int) and value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
