#!/usr/bin/python3
# Made by MEGATRON
"""

writes to text file &  returns num chars written
"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
