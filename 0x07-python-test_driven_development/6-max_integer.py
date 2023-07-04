#!/usr/bin/python3

# Made By MEGATRON

"""Module to find the max intg in a list"""


def max_integer(list=[]):
    """Funct to find & return the max intg in a list of intgs"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
