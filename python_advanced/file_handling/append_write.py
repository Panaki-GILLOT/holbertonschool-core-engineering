#!/usr/bin/env python3
"""
Append a string at the end of a UTF-8 text file
"""


def append_write(filename="", text=""):
    """Appends a string to a file and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
