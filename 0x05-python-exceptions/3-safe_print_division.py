#!/usr/bin/python3

def safe_print_division(a, b):
    '''Divides 2 integers and prints the result, using exception handling.'''

    try:
        div = a/b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
