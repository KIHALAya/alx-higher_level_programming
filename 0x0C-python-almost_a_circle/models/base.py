#!/usr/bin/python3
""" Base - manage id attribute in all future classes
and avoid duplicating the same code """


class Base:
    """ The “base” of all other classes in this project

    Attributes:
       __nb_objects : number of objects of the class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance.

        Args:
            id : the id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
