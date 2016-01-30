# -*- coding: utf-8 -*-
__author__ = 'lihui'

# 8-2
def a_range(f, t, i):
    return range(f, t, i)


# 8-4
def is_prime(num):

    count = num / 2
    while count != 0:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True