# -*- coding: utf-8 -*-

from socket import *

HOST = "localhost"
PORT = 8881
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClisock = socket(AF_INET, SOCK_STREAM)
tcpClisock.connect(ADDR)

while True:
    data = raw_input(">")
    if not data:
        break
    tcpClisock.send(data)
    data = tcpClisock.recv(BUFSIZ)
    if not data:
        break
    print data
