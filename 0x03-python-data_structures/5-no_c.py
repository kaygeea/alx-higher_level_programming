#!/usr/bin/python3

def no_c(my_string):
    '''This function removes all characters c and C from a string.'''

    no_c_str = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            no_c_str += c
    return (no_c_str)
