#!/usr/bin/python3
"""A script that fetshes url"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        con = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content: {}".format(con.decode('utf-8')))
