# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This code is a part of Lab Assignment #2 TCP file Transfer. This file utilizes Threads  

import socket, sys, re, time, os
sys.path.append("../lib")
import params
from socketFramed import framedSocket
import threader

switchesVarDefaults = (
    (('-l','--listenPort'),'listenPort', 50001),
    (('-?','--usage'),"usage",False),
    )

progname = "echoserver"
paramMap = paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = '' # all available interfaces 

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create new socket, stream = 2 way  
s.bind((listenAddr,listenPort)) # attach socket to fd,      local host 50001
s.listen(1) # listen for new connections 


while True: # For every connection
    conn,addr = s.accept()
    threader.Worker(conn,addr).start()
    
    
