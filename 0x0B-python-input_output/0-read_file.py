#!/usr/bin/python3
# Made by MEGATRON
"""

Reads &  prints contents from file
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
