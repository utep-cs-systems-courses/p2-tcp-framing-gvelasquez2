# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This code is a part of Lab Assignment #2 TCP file Transfer. This code uses a fork based Server.
# It was built from the demo code provided by Dr. Freudenthal.

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
listenAddr = '' # all available interfaces 

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create new socket, stream = 2 way  
s.bind((listenAddr,listenPort)) # attach socket to fd,      local host 50001
s.listen(1) # listen for new connections 


while True: # For every connection
    conn,addr = s.accept()
    fs = framedSocket(conn)
    
    if os.fork()==0: # Fork off a child to become server  
        contents = (fs.receiveMessage()) # get command from client 

        filename = contents
        
        if os.path.isfile(filename): # Check if there is already a file named filename 
            fs.sendMessage(b"NO")
            conn.shutdown(socket.SHUT_WR)
        else:
            fs.sendMessage(b"OK")

        fd = os.open(filename, os.O_CREAT | os.O_WRONLY) # open the file, so it can be written to 
        os.write(fd,fs.receiveMessage().encode())
        os.close(fd)
