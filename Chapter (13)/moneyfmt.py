# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 13-3
class MoneyFmt(object):

    def __init__(self, value=0.0):
        self.value = float(value)


    def dollarize(self, mark=0):
        list_num = list(str(self.value))
        str_num = str(self.value)

        if self.value < 0:
            str_num = str_num[1:]
            list_num = list(str_num)

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
            return "-$%s" % result
        else:
            return "$<%s>" % result


    def update(self, new_value):
        self.value = new_value


    def __nonzero__(self):
        if self.value != 0:
            return True


    def __repr__(self):
        return str(self.value)


    def __str__(self):
        return self.__class__.dollarize(self)
