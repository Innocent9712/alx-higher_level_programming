#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
You must use requests
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
