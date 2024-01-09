#!/usr/bin/python3

""Read-only function""

def read_file(filename=""):
	with open(filename, encoding='UTF8') as file:
		print(file.read(), end="")
