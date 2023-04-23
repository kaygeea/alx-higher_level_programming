#!/usr/bin/python3
'''This module builds a function that converts a Roman numeral to an int'''
import roman


def roman_to_int(roman_string):
    '''this function coverts a Roman numeral to an int'''

    if roman_string:
        roman_num = roman.fromRoman(roman_string)
    return roman_num
