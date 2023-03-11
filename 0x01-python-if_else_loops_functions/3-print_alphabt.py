#!/usr/bin/python3
for alphs in range(97, 123):
    if alphs == 101 or alphs == 113:
        continue
    print("{}".format(chr(alphs)), end="")
