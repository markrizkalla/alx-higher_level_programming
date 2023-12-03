#!/usr/bin/python3
""" script that takes in URL
send resques to the URL"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
