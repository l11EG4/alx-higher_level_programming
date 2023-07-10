#!/usr/bin/python3
# Made by MEGATRON
"""
Module 8-rectangle

Contains parent class BaseGeometry
with pub instance method area and integer_validator

Contains subclass Rectangle
with instantiation of private attributes width and height, valid by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
