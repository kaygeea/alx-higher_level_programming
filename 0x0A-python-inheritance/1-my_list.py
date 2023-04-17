#!/usr/bin/python3
'''This module creates a func that derives from another.'''


class MyList(list):
    '''This class derives from the class 'list'.'''

    def print_sorted(self):
        '''This function prints an ascending sorted list'''

        print(sorted(self))
