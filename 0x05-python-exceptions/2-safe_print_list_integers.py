#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''Prints the first x elements of a list and only integers, using EH.'''

    count = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
