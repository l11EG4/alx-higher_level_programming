#!/usr/bin/python3
# Made by MEGATRON
"""
Module 101-add_attribute

Contains a funct that adds new attribute if possible
"""


def add_attribute(obj, attribute, value):
    """
    add attribute to object if possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
