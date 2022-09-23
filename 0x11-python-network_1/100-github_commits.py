#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
from sys import argv
url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits?per_page=10"
res = requests.get(url)
try:
    my_data = res.json()
    # print(my_data)
    for row in my_data:
        print(f"{row['sha']}: {row['commit']['author']['name']}")
except Exception:
    print("None")
