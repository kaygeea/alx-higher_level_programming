#!/usr/bin/python3
'''This module creates a func that returns a list of obj's attrs and meths.'''


def lookup(obj):
    '''This func returns a list of obj's attributes and methods.'''
    attsNmeths = [dir(obj)]

    return attsNmeths
