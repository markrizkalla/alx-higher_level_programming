#!/usr/bin/python3
"""Define a file-appending func"""


def append_write(filename="", text=""):
    """Appends a string to end of file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
