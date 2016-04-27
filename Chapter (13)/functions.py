# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 13-4
class UserDatabase(object):
    import shelve
    def __init__(self, username, pwd):
        # 读取数据库，如果没有则新建db
        db = {}
        # 验证用户名和密码
        print "New user in!"


    def db_add(self):
        pass


    def db_del(self):
        pass


    def db_change(self):
        pass


    def __del__(self):
        pass


# 13-5
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print "(%s, %s)" % (self.x, self.y)


# 13-6
class Line(object):

    def __init__(self, x1=0, x2=0, y1=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.length = self.length()
        self.slope = self.slope()

    def __str__(self):
        return "(%s, %s)" % ((self.x1, self.y1), (self.x2, self.y2))

    __repr__ = __str__

    def length(self):
        import math
        return math.sqrt((self.x2-self.x1) ** 2 + (self.y2-self.y1) ** 2)

    def slope(self):
        try:
            return (self.y2-self.y1) / float((self.x2-self.x1))
        except ZeroDivisionError:
            return None


# 13-7
from time import time, ctime, localtime, strftime


class TimeWarp(object):

    def __init__(self, now_time=time()):
        self.time = now_time

    def display(self, time_format=None):

        if time_format is None:
            return ctime(self.time)

        if time_format == "MDY":
            return strftime("%m/%d/%y", localtime(self.time))
        elif time_format == "MDYY":
            return strftime("%m/%d/%Y", localtime(self.time))
        elif time_format == "DMY":
            return strftime("%d/%m/%y", localtime(self.time))
        elif time_format == "DMYY":
            return strftime("%d/%m/%Y", localtime(self.time))
        elif time_format == "MODYY":
            return strftime("%a %d, %Y", localtime(self.time))

    def update(self, new_time=time()):
        self.time = new_time


# 13-8
class Stack(list):

    def push(self, value):
        self.append(value)

    def isempty(self):
        if len(self) == 0:
            return 1
        else:
            return 0

    def peek(self):
        return self[0]

    # if "pop" not in dir(self):


test = Stack()
test.push("hi")
test.push("hello")
test.push("hola")
test.peek()
print test
test.pop()
print test
print test.isempty()
print dir(test)


# 13-9
class Queue(list):

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        return self.pop(0)

    def isempty(self):
        if len(self) == 0:
            return 1
        else:
            return 0

    def peek(self):
        return self[0]


# 13-10
class StackQueue(list):

    def shift(self):
        return self.pop(0)

    def unshift(self, value):
        self.insert(0, value)

    def push(self, value):
        self.append(value)

    def pop(self, index=None):
        return self.pop()



