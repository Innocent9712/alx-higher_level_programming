#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
You must use requests and sys
"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except requests.HTTPError:
        print(f"Error code: {res.status_code}")
