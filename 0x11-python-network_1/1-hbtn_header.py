#!/usr/bin/python3
"""script that takes in a URL , sends a requesr to the URL"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
