#!/usr/bin/python3
# Made by MEGATRON
"""

returns JSON representation of object (string)
"""


def to_json_string(my_obj):
    """Returns: JSON representation of object (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
