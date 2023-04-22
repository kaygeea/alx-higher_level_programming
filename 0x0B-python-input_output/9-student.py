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

    def to_json(self):
        '''This method retrieves a dict representation of a student() object'''

        return self.__dict__
