#!/usr/bin/python3
"""
   Contains a script that sends a GET request and displays the body of the
   response. If the HTTP status code => 400, it prints the error code instead.

   USAGE: ./7-error_code.py <URL>
"""
import requests
from sys import argv


if __name__ == "__main__":
    resp_object = requests.get(argv[1])

    if resp_object.status_code >= 400:
        print("Error code: {}".format(resp_object.status_code))
    else:
        print(resp_object.text)
