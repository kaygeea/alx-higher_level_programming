#!/usr/bin/python3
def islower(c):
    """Checks if a char is lowercase. Returns: True if so; and False if not"""
    c = ord(c)
    if c >= 97 and c <= 122:
        return True
    else:
        return False
