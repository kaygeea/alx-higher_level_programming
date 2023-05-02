#!/usr/bin/python3
'''This module creates a string indentation function'''


def text_indentation(text):
    '''This function breaks a text by adding 2 new lines after any of the
        the following delimiters: '.', '?' & ':' and prints the new text.
    Args:
        text (str): incoming argument for text to be operated on.
    Exception:
        TypeError: if text is not a string.
    Condition:
        No space at the beginning or at the end of each printed line.
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
