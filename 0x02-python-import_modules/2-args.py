#!/usr/bin/python3

if __name__ == "__main__":
    '''This program prints the number of, and the list of its arguments'''
    import sys

    numArgs = len(sys.argv)
    if numArgs == 1:
        print("{} arguments.".format(numArgs -1))
    elif numArgs == 2:
        print("{} argument:".format(numArgs -1), end='\n')
        print("{}: {}".format((numArgs -1), sys.argv[1]))
    else:
        if numArgs > 2:
            print("{} arguments:".format(numArgs -1, end='\n'))
            for i in range(1, numArgs):
                print("{}: {}".format(i, sys.argv[i]))
