#!/usr/bin/python3
"""
 A Python script that takes in a URL, sends a request to 
 the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
from sys import argv

try:
    urllib.request.urlopen(argv[1])
    with urllib.request.urlopen(argv[1]) as response:
        print(response.read().decode('utf8'))
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")