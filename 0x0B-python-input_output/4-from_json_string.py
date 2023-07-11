#!/usr/bin/python3
# Made by MEGATRON
"""

returns: python data structure from JSON str
"""


def from_json_string(my_str):
    """Returns python data structure from JSON str
    Args:
        my_str: json str representation
    Return:
        python object
    """
    import json

    return json.loads(my_str)
