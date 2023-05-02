#!/usr/bin/python3
"""This module creates a square printing function"""


def print_square(size):
    """This function prints a square with the '#' character.
    Args:
        size: incoming argument for the size length of the sqaure
    Exceptions:
        TypeError: a. if size is not an integer; and
                    b. if size is a float and is less that 0.
        ValueError: if size is less that 0
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if isinstance(size, int):
        for height in range(0, size):
            [print("#", end="") for width in range(size)]
            print("")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
