# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 13-3
class MoneyFmt(object):

    def __init__(self, value):
        self.value = value


    def dollarize(self, mark=0):
        list_num = list(str(self.value))
        str_num = str(self.value)

        if isinstance(self.value, float):
            dot = str_num.find(".")
        else:
            dot = len(str_num)

        for i in range(dot, 0, -3):
            if i != dot:
                list_num.insert(i, ",")
        result = "".join(list_num)

        if self.value >= 0:
            return "$%s" % result
        elif self.value < 0 and mark == 0:
            return "-$%s" % result[1:]
        else:
            return "$<%s>" % result[1:]


    def update(self, new_value):
        self.value = new_value


    def __nonzero__(self):
        if self.value != 0:
            return True


    def __repr__(self):
        return float(self.value)


    def __str__(self):
        return MoneyFmt.dollarize(self.value)


s = MoneyFmt(123456789)
print s.dollarize()
print s.__nonzero__()
s.update(-9876543210.34)
print s.dollarize()


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

