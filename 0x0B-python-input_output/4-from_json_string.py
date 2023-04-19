#!/usr/bin/python3
'''This module builds a function that does JSON deserialization'''
import json


def from_json_string(my_obj):
    '''This function returns a Python obj represented by a JSON string.
    Args:
        my_obj: incoming argument for JSON string to be deserialized.
    Return:
        my_obj: Python object.
    '''
    return json.loads(my_obj)
