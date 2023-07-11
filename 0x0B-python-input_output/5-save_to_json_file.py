#!/usr/bin/python3
# Made by MEGATRON
"""

writes Python object to file using JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """Writes Python object to file using JSON represenation
    Args:
        my_obj: python obj
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
