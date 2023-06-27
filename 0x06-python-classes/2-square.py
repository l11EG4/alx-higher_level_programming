#!/usr/bin/python3

# made by Megatron

"""Define a class Squar"""


class Square:
    """Represent a squar"""

    def __init__(self, size=0):
        """Initialize a new Squar

        Args:
            size (int): the size of the new squar
        """
        if not isinstance(size, int):
            raise TypeError("the size must be an integ")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size
