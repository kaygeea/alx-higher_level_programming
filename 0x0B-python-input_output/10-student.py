#!/usr/bin/python3
'''This module builds a class'''


class Student:
    '''This class defines a student'''

    def __init__(self, first_name, last_name, age):
        '''This inistializes a Student class
        Args:
            first_name: incoming argument for first name of a student() object
            last_name: incoming argument for last name of a student() object
            age: incoming argument for the age of a student() object
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''This func returns the dict representation of a simple data stuct.
        Description:
                    If attrs is a list of strings, only attribute names
                    contained in this list must be retrieved
        Arg:
            attrs: (str) incoming argument for attribute to be represented.'''

        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
