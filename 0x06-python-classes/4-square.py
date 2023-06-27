#!/usr/bin/python3

# Made by MEGATRON

"""Define a class Squar"""


class Square:
    """Represent a squar"""

    def __init__(self, size=0):
        """Init a new squar

        Args:
            size (int): size of the new squar
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the squar"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("the size must be an integ")
        elif value < 0:
            raise ValueError("the size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the squar"""
        return (self.__size * self.__size)
