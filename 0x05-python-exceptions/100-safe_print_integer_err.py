#!/usr/bin/python3

def safe_print_integer_err(value):
    '''Prints an integer, using advanced exception handling'''
    import logging

    try:
        print("{:d}".format(value))
        return (True)
    except Exception as err:
        print(logging.exception)
        return (False)
