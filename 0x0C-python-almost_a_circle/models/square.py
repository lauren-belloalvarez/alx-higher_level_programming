#!/usr/bin/python3
"""Defining class for a square"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """New square
        Arguments:
        size : size of square
        x : x co-ord. of square
        y : y co-ord of square
        id : squares identity
        """
        super().__init__(size, size, x, y, id)

    """Getters and setters"""
    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
