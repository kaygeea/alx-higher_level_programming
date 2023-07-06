#!/usr/bin/python3
"""Build a script to send POST request to a URL of an email to a URL,
and display the body of the response (decoded in utf-8)

USAGE: ./2-post_email.py <URL> <email>
"""
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    data_to_post = {'email' : argv[2]}
    encoded_data = urlencode(data_to_post).encode('utf-8')
    post_req = Request(argv[1], data=encoded_data)

    with urlopen(post_req) as response:
        decoded_data = response.read().decode('utf-8')
        print(decoded_data)
