#!/usr/bin/python3

def best_score(a_dictionary):
    '''This func returns a key with the biggest integer value'''
    if a_dictionary is not None:
        return (max(a_dictionary, key=a_dictionary.get))
    return None