#!/usr/bin/python3
# Made by Megatron
"""
Module 2-is_same_class

Contains method is_same_class
returns a True if obj is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes to
        use issubclass() to get what obj is a subclass of

    Return:
        True if object is exactly an instance of specified class
    """
    return type(obj) == a_class
