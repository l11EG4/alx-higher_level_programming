#!/usr/bin/python3

# Made by Megatron

"""Define a class Squar"""


class Square:
    """Represent a squar"""

    def __init__(self, size=0):
        """Init a new squar

        Args:
            size (int): size of the new squar
        """
        if not isinstance(size, int):
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the squar"""
        return (self.__size * self.__size)
