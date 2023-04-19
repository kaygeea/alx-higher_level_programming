#!/usr/bin/python3
'''This module builds a func that writes to a text file'''


def write_file(filename="", text=""):
    '''This function writes to a .txt and returns count of chars written'''

    with open(filename, 'w', encoding="utf-8") as fl:
        if not isinstance(text, str):
            text = str(text)
            return (fl.write(text))
        else:
            return (fl.write(text))
