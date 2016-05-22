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
# 读取数据库，获取最后一个用户的id
user_data = {"0":("lihui")}
user_id_list = [0]
room_id_list = [0]

class User(object):
    def __init__(self, name, sex=None, age=None, hobby=None):
        self.name = name
        self.sex = sex
        self.age = age
        self.hobby = hobby
        self.msg = Message()
        self.room = Room()
        self.msg.append(self.name)
        self.room.append(self.name)
        last_id = user_id_list[-1]
        self.id = last_id + 1
        user_id_list.append(self.id)
        user_data[self.id] = self, self.name, self.sex, self.age, self.hobby

    def info(self):
        info =  """
        name: %s
        sex: %s
        age: %d
        hobby: %s
        """ % (self.name,self.sex, self.age, self.hobby)

        return info


class Message(list, User):
    # a msg list class
    def send(self, msg, to):
        send_time = "[" +time.asctime() + "]"
        to.msg.append(self[0] + " " + send_time + "\n" + msg)

    def receive(self):
        number =  len(self) - 1
        print "%d message unread." % number
        while len(self) > 1:
            msg =  self.pop()
            print msg

class Room(list, User):
    
    def create(self):
        last_room_id = room_id_list[-1]
        self.id = last_room_id + 1
        room_id_list.append(self.id)
        self.time = time.asctime()
        print "Room created!"
        print "Room ID: %d" % self.id
        print self
        
    def invite(self, user_id):
        self.append(user_id)

    def kick(self, user_id):
        self.remove(user_id)

    def show_user(self):
        for user_id in self:
            print user_data[user_id][0]

    def info(self):
        print """
        Room ID: %d
        create time: %s
        user: %s
        """ % (self.id, self.time, "")#",".join([user_data[user_id][0] for user_id in self]))

    def talk(self, msg):
        talk_time = "[" +time.asctime() + "]"
        print self[0]
        for user_id in self[1:]:
            print user_id
            user_data[user_id][0].msg.append(self[0] + " " + talk_time + "\n" + msg)
            
print "-------------------info-test--------------"
lihui = User("lihui", "boy")
lihui.age = 20
lihui.hobby = "code"

weiyao = User("weiyao", "girl", 21, "English")

print lihui.info()
print weiyao.info()

print "-----------------msg-test-------------------"

lihui.msg.send("hi, weiyao", weiyao)
lihui.msg.send("Where are you?", weiyao)
weiyao.msg.receive()
print "------------------"
weiyao.msg.send("hello, lihui", lihui)
weiyao.msg.send("hello, I am in computer lab", lihui)
lihui.msg.receive()

print "-----------------room-test----------------------"

lihui.room.create()
lihui.room.invite(1)
# lihui.room.info()
# lihui.room.show_user()
lihui.room.talk("hi, everyone!")
weiyao.msg.receive()
lihui.msg.receive()
# lihui.room.kick(1)
print lihui.room

print "----------------------------datd---------------------"
for id in user_data.keys():
    print id, user_data[id]

print user_id_list

print room_id_list
