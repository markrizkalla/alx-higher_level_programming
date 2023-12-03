#!/usr/bin/python3
"""script that takes in a URL and display the bodt of the response"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print('Error code:', e.code)
