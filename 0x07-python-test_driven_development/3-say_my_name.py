#!/usr/bin/python3
'''This module builds a function that prints out a string'''


def say_my_name(first_name, last_name=""):
    '''This func prints the string "My name is <first name> <last name>"
        
        Args:
            first_name: incoming argument for first name of name to be printed
            last_name: incoming argument for last name of name to be printed
        
        Exception:
            TypeError: if either first_name or last_name are not strings
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        if isinstance(first_name, str) and isinstance(last_name, str):
            print("My name is {} {}".format(first_name, last_name))
