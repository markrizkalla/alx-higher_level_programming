#!/usr/bin/python3
""" Script that takes in a URL and email and sends a POST request"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
