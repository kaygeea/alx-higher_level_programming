#!/usr/bin/python3
"""This module creates a fun that finds a peak in a list of unsorted ints"""


def find_peak(list_of_integers):
    """Find the peak in (unsorted) list_of_integers"""
    size = len(list_of_integers)

    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid_val = int(size / 2)
    mid_idx = list_of_integers[mid_val]

    if (mid_idx > list_of_integers[mid_val - 1] and
            mid_idx > list_of_integers[mid_val + 1]):
        return mid_idx
    elif mid_idx <= list_of_integers[mid_val - 1]:
        return find_peak(list_of_integers[:mid_val])
    else:
        return find_peak(list_of_integers[mid_val + 1:])
