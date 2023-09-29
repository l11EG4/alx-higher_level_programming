#!/usr/bin/python3
# amde by MEGA
"""
Displays the X-Request-Id header variable of a request to a given URL
"""

from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
