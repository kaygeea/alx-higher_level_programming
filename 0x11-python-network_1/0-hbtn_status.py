#!/usr/bin/python3
"""This module builds a script that fetches a given URL."""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    alx_url = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(alx_url) as response_obj:
        body = response_obj.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
