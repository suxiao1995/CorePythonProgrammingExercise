# -*- coding: utf-8 -*-
__author__ = 'lihui'

# 12-5
def test():
    time = __import__('time')

    return time.asctime()

def test2():
    asc = __import__('time', ['asctime'])
    return asc.asctime()

# 12-5
def importAs(modulename):
    return __import__(modulename)

