#!/usr/bin/python3

"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
        The number of characters written.
    """
	with open(filename, "w", encoding="utf-8") as f:
		return f.write(text)

