#!/usr/bin/python3
'''This module builds a function that performs JSON serialization'''
import json


def save_to_json_file(my_obj, filename):
    '''This function serializes an object and saves the JSON rep to a file'''

    with open(filename, "w") as j_rep:
        json.dump(my_obj, j_rep)
