#!/usr/bin/python3

#made by Megatron

import sys


def safe_function(fct, *args):
    """Execut funct safely.

    Args:
        fct: funct to execute.
        args: Arg for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
