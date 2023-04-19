#!/usr/bin/python3
'''This module builds a function that appends to a text file'''


def append_write(filename="", text=""):
    '''This function writes to a .txt and returns count of chars written
    Args:
        filename: incoming argument for file to be appended to
        text: incoming argument for content to be appended to filename
    '''
    with open(filename, 'a', encoding="utf-8") as fl:
        if not isinstance(text, str):
            text = str(text)
            return (fl.write(text))
        else:
            return (fl.write(text))
