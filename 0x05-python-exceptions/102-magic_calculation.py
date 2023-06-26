#!/usr/bin/python3

# Made by Megtron

def magic_calculation(a, b):
    results = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                results += a ** b / i
        except:
            results = b + a
            break
    return (results)
