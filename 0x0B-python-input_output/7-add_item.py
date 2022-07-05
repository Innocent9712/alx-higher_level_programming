#!/usr/bin/python3
"""
    module to add items to a list and save the list
    as a json string
"""

import os
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_is_present = os.path.exists("add_item.json")
if not file_is_present:
    save_to_json_file([], "add_item.json")

if len(sys.argv) < 2:
    exit(0)

my_list = load_from_json_file("add_item.json")
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, "add_item.json")
