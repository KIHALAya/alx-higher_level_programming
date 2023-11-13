#!/usr/bin/python3
""" Base Module """
import json
import csv


class Base:
    """ Base class with class methods for handling JSON and CSV strings """

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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of dictionaries represented by json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dicts = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes list_objs to CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes CSV file to a list of instances """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = [cls.create(*row) for row in reader]
                return instances
        except FileNotFoundError:
            return []
