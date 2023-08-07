#!/usr/bin/python3
'''This module builds a class'''


class BaseGeometry:
    '''Create a class BaseGeometry'''

    pass

    def area(self):
        '''Raises an Exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate incoming arg - value
        Args:
            name: incoming arg for name of item to which value is assigned
            value: incoming arg for value of name
        Exceptions:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        '''
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        elif isinstance(value, int) and value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        else:
            self.value = value
