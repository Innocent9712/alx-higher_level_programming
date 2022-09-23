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

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}"
    url = url + "/commits?per_page=10"
    res = requests.get(url)
    try:
        my_data = res.json()
        # print(my_data)
        for row in my_data:
            sha = row.get('sha')
            author_name = row.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except Exception:
        print("None")
