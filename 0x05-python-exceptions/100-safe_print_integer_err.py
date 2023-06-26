#!/usr/bin/python3

import sys

# Made by Megatron

def safe_print_integer_err(value):
    """Prints an intg with "{:d}".format().

    If a ValueError msg is caught, a corresponding
    msg is printed to standard error.

    Args:
        value (int): The intg to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
