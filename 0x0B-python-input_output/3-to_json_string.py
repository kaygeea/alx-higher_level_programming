#!/usr/bin/python3
'''This module builds a function that does JSON serialization'''
import json


def to_json_string(my_obj):
    '''This function returns the JSON representation of a string object.

    Args:
        my_obj: incoming argument for sting object to be serialized.

    Return:
        JSON representation of my_obj.
    '''

    with open("my_obj", "r+", encoding="utf-8") as str_rep:
            return json.dumps(my_obj)
