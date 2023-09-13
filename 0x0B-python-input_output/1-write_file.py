#!/usr/bin/python3
"""Define write to a file fun"""


def write_file(filename="", text=""):
    """ fun to write text into filename and tell Char no."""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return (f.tell())
