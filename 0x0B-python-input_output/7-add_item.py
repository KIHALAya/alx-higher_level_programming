#!/usr/bin/python3
"""Script to append command line arguments
to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    save_to = __import__('5-save_to_json_file').save_to
    load_from = \
        __import__('6-load_from_json_file').load_from

    try:
        items = load_from("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to(items, "add_item.json")
