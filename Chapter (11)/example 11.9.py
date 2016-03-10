# -*- coding: utf-8 -*-
__author__ = 'lihui'


j, k = 1, 2


def proc1():

    j, k = 3, 4
    print "j == %d and k == %d" % (j, k)
    k = 5


def proc2():

    j = 6
    proc1()
    print "j == %d and k == %d" % (j, k)


k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8
proc2()
print "j == %d and k == %d" % (j, k)

# output:
# j = 3 k =4
# j = 1 k =7
# j = 3 k =4
# j = 6 k =7
# j = 8 k =7



