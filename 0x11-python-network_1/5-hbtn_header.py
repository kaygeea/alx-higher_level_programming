#!/usr/bin/python3
"""Contain a script that GETs a URL and display a specified header variable"""
import requests
from sys import argv


if __name__ == "__main__":
    resp_obj = requests.get(argv[1])
    print(resp_obj.headers['x-request-id'])  # case-insensitivity
