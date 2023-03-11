#!/usr/bin/python3
for nums in range(0, 100):
    if not (nums == 99):
        print("{:02d}".format(nums), end=', ')
    elif nums == 99:
        print("{:02d}".format(nums), end="\n")
