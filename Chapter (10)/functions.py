# -*- coding: utf-8 -*-
__author__ = 'lihui'

# 10-6
def safe_open(filename, mode='r'):
    try:
        f = open(filename, mode)
    except:
        f = None
    return f


# 10-7
def safe_input():
    try:
        words = raw_input()
    except:
        words = None
    return words


# 10-8
def safe_sqrt(x):
    import math, cmath
    try:
        result = math.sqrt(x)
    except ValueError:
        result = cmath.sqrt(x)
    return result


