# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This code ...

import socket, sys, re, time, os
sys.path.append("../lib")
import params
from socketFramed import framedSocket

switchesVarDefaults = (
    (('-l','--listenPort'),'listenPort', 50001),
    (('-?','--usage'),"usage",False),
    )

progname = "echoserver"
paramMap = paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((listenAddr,listenPort))
s.listen(1)

while True:
    conn,addr = s.accept()
    fs = framedSocket(conn)
    if os.fork()==0:
        print("Connected by", addr)
        contents = fs.recieveMessage()
        print(contents[1])
