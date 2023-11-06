#!/usr/bin/python3
"""MyList - A class that inherits from list and provides
a method to print the list in sorted order"""


class MyList(list):
    """
    MyList class inherits from list and provides a print_sorted method
    """

    def print_sorted(self):
        """
        Print the list in sorted (ascending) order
        """
        sorted_list = sorted(self)
        print(sorted_list)
