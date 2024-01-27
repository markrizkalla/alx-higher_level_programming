#!/usr/bin/python3
"""list the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url =f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    r = requests.get(url)
    for i in range(10):
        print(r.json()[i].get('sha'),end = " ")
        print("".join(r.json()[i].get('commit').get('author').get('name')))
