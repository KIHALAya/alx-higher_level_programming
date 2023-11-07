#!/usr/bin/python3
"""Student Class - Defines a student by first_name, last_name, and age"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class


class Student:
    """A class representing a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)
        return student_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the
        Student instance with the provided dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
