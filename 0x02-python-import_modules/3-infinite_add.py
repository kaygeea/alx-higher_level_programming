#!/usr/bin/python3

if __name__ == "__main__":
    '''This program prints the result of the addition of all arguments'''
    import sys

    numArgs = len(sys.argv)
    sum = 0

    for i in range(1, numArgs):
        sum += int(sys.argv[i])
    print("{}".format(sum))
