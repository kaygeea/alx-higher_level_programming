#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list, using exception handling'''
    count = 0
    for elem in range(x):
        try:
            print("{}".format(my_list[elem]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
