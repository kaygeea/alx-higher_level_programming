#!/usr/bin/python3
'''This module builds a function that performs JSON deserialization'''
import json


def load_from_json_file(filename):
    '''This function deserializes a JSON file and creates and object'''

    with open(filename, "r") as j_rep:
        data = json.load(j_rep)
        return data
