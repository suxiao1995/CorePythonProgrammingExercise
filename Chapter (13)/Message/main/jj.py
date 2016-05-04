# -*- coding: utf-8 -*-
import time
import random

__author__ = 'lihui'

# todo 存储用户数据
# todo 存储消息记录
# todo 存储未上线用户收到的信息
# todo 签名档
# todo 多人聊天室

# 13-12
class User(object):
    user_id = 0
    def __init__(self, name, age=None, hobby=None):
        self.msg = Message()
        self.room = Room()
        self.name = name
        self.age = age
        self.hobby = hobby
        self.msg = Message()
        self.id = User.user_id
        User.user_id += 1

    def info(self):
        info =  """
        name: %s
        age: %d
        hobby: %s
        """ % (self.name, self.age, self.hobby)

        return info


class Message(list, User):

    def send(self, msg, to):
        send_time = "[" +time.asctime() + "]"
        to.msg.append(msg + "\n" + send_time)

    def receive(self):
        print "%d message unread." % len(self)
        while len(self) > 0:
            msg =  self.pop()
            print msg

class Room(list):

    def create(self):
        self.id = random.randint(1, 1000)
        self.time = time.asctime()
        print "Room crated!"
        print "Room ID: %d" % self.id

    def invite(self, user):
        self.append(user)

    def kick(self, user):
        self.remove(user)

    def show_user(self):
        for user in self:
            print user

    def info(self):
        print """
        Room ID: %d
        create time: %s
        user: %s
        """ % (self.id, self.time, ",".join(self))

    def talk(self, msg):
        talk_time = "[" +time.asctime() + "]"
        for user in self:
            user.msg.append(msg + talk_time)

print "-------------------info-test--------------"
lihui = User("lihui")
lihui.age = 20
lihui.hobby = "code"
weiyao = User("weiyao", 21, "English")

print lihui.info()
print weiyao.info()

print "-----------------msg-test-------------------"
lihui.msg.send("hi, weiyao", weiyao)
lihui.msg.send("Where are you?", weiyao)
weiyao.msg.receive()
print "------------------"
weiyao.msg.send("hello, lihui", lihui)
weiyao.msg.receive()

print "-----------------room-test----------------------"
lihui.room.create()
lihui.room.invite("weiyao")
lihui.room.info()
lihui.room.show_user()
lihui.room.talk("hi, everyone!")
lihui.room.kick("weiyao")