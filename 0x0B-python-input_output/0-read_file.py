#!/usr/bin/python3
'''This module builds a function that reads and prints from a text file'''


def read_file(filename=""):
    '''This function reads from a text file and prints to stdout'''

    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end='')
