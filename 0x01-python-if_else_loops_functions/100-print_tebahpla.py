#!/usr/bin/python3
for s in reversed(range(97, 123)):
    print("{:c}.format(s if (s % 2 == 0) else (s - 32)), end='')
