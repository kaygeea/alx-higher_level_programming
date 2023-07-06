#!/usr/bin/python3
"""
   Build a script to send a GET request and display the body of the response,
   while managing exceptions raised by .HTTPError to print error code.

   USAGE: ./3-error_code.py <URL>
"""
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    try:
        req_url = Request(argv[1])

        with urlopen(req_url) as resp_object:
            print(resp_object.read().decode('utf-8'))
    except HTTPError as req_error:
        print("Error code: {}".format(req_error.status))
