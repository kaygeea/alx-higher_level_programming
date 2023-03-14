#!/usr/bin/python3
if __name__ == "__main__":
    """Imports a func from a file and prints the result of its exec'n."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
