#!/usr/bin/python3
""" Base Module """
import json


class Base:
    """ Base class with a static method to_json_string """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance with an id

        Args:
            id (int): id of the Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
