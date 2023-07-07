#!/usr/bin/python3
"""Build a script that uses the Requests package to fetch a given URL"""
from requests import get


if __name__ == "__main__":
    req_url = get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(req_url.text)))
    print("\t- content: {}".format(req_url.text))
