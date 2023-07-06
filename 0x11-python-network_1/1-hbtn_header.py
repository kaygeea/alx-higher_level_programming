#!/usr/bin/python3
"""Build a script to GET a URL and display a specified header variable"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    arg_url = argv[1]
    with urllib.request.urlopen(arg_url) as response_obj:
        header = response_obj.info()
        print(header.get('X-Request-Id'))
