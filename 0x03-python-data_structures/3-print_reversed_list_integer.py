#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''This function prints all integers of a list, in reverse order.'''

    if my_list:
        my_list.reverse()
        for nums in my_list:
            print("{:d}".format(nums))
