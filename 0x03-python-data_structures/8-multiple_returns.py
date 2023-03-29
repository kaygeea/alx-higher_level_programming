#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character'''

    new_tup = ()

    if len(sentence) == 0:
        new_tup = 0, 'None'
    else:
        new_tup = len(sentence), sentence[0]
    return new_tup
