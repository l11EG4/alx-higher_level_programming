#!/usr/bin/python3
# Made by MEGATRON
"""

creates a Python object from JSON file
"""


def load_from_json_file(filename):
    """Creates a Python object from JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
