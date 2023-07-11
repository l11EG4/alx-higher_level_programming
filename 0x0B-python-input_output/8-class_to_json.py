#!/usr/bin/python3
# Made by MEGATRON
"""

Contains funct that
returns: dictionary description with simple data structure
(list, dictionary, dictionary, string)
for JSON serialization of an obj
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
       (list, dictionary, dictionary, string)
       for JSON serialization of an obj
    Args:
        obj: python obj
    """
    return obj.__dict__
