#!/usr/bin/python3
"""Script to append command line arguments to a
Python list and save them to a file."""

import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        stored_items = load_from_json("add_item.json")
    except FileNotFoundError:
        stored_items = []
    stored_items.extend(sys.argv[1:])
    save_to_json(stored_items, "add_item.json")
