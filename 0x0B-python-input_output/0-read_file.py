#!/usr/bin/python3
"""read file data and print them"""


def read_file(filename=""):
    """func to read and print data in file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
