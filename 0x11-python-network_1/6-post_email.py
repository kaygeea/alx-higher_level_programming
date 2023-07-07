#!/usr/bin/python3
"""
   Contains a script that sends a POST request to a URL of an email to a URL,
   and displays the body of the response.

   USAGE: ./6-post_email.py <URL> <email>
"""
import requests
from sys import argv


if __name__ == "__main__":
    post_req = requests.post(argv[1], data={'email': argv[2]})
    print(post_req.text)
