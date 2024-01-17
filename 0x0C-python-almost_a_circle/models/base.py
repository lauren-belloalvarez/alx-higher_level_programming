#!/usr/bin/python3
"""Base Module"""

import json
import csv


class Base:
    """Defines base model classess for entire project
        Attributes:
                   __nb_objects : int, number of bases
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor that initialises new Base
        Arguments:
                    id : int, identity of new base
                    """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects

