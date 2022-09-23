#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

url = "http://0.0.0.0:5000/search_user"
values = {
    "q": ""
}

try:
    values["q"] = argv[1]
except IndexError:
    pass

res = requests.post(url, data=values).json()
if res == {}:
    print("No result")
else:
    print(f"[{res['id']}] {res['name']}")
