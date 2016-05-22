# -*- coding: utf-8 -*-
__author__ = 'lihui'

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "Waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "...connection from:", addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data or data == "q":
            tcpCliSock.close()
            break
        print data
        # msg = data.split()
        # print "Receive message from: %s" % msg[0]
        # print "Send message to: %s" % msg[2]
        msg = raw_input(">")
        tcpCliSock.send("[%s] %s" % (ctime(), msg))