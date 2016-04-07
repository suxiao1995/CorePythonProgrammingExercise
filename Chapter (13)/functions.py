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


#