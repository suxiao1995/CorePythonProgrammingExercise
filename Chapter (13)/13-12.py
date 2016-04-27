# -*- coding: utf-8 -*-
__author__ = 'lihui'


# 13-12
class Message(object):

    def send(self, msg, to):
        pass

    def receive(self):
        pass


class User(object):
    user_id = 0
    def __init__(self, name, age=None, hobby=None):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.msg = Message()
        self.id = User.user_id
        User.user_id += 1

    def get_info(self):
        info =  """
        name: %s
        age: %d
        hobby: %s
        """ % (self.name, self.age, self.hobby)

        return info

    def inbox(self):
        mailbox = {self.id:[]}


class Room(object):

    def __init__(self):
        pass

    def creat(self):
        pass

    def invite(self, id):
        pass

    def show_info(self):
        pass


