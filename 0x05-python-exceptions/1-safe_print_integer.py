#!/usr/bin/python3

def safe_print_integer(value):
    '''Prints an integer, using exception handling'''
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)           
