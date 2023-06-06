#!/usr/bin/python3
def uppercase(str):
    upp = ''
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
    upp = upp + c
    print('{}'.format(upp))
