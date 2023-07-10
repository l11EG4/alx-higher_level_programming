#!/usr/bin/python3
# Made By MEGATRON
"""
Module 3-is_kind_of_class

Contains the method is_kind_of_class
returns True if obj is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Return:
        True if object is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
