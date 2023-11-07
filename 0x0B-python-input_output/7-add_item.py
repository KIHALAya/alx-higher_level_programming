#!/usr/bin/python3
import sys
from os import path

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = 'add_item.json'

if not path.exists(filename):
    data = []
else:
    data = load_from_json_file(filename)

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
