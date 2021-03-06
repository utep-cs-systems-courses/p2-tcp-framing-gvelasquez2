# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This file is a part of Lab Assignment #2 TCP File Transfer. This file act as the Client and
# is built from the demo code provided by Dr. Fruedenthal. 

import socket,sys,re,time,os
sys.path.append("../lib")
import params
from read import my_getLine
from read import parseTCPInput
from socketFramed import framedSocket 

switchesVarDefaults = (
    (('-s','--server'),'server',"127.0.0.1:50001"),
    (('-d','--delay'),'delay',"0"),
    (('-?','--usage'),"usage",False),
    )

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server,usage = paramMap["server"],paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost,serverPort = re.split(":",server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype,proto,canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af,socktype,proto))
        s = socket.socket(af,socktype,proto)
    except socket.error as msg:
        print(" error %s" % msg)
        s = None
        continue
    try:
        print("attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None: # failed 
    print("could not open socket")
    sys.exit(1)

delay = float(paramMap['delay'])
if delay != 0:
    print(f"sleeping for {delays}s")
    time.sleep(delay)
    print("done sleeping")

    
fs = framedSocket(s)

input = my_getLine()
command,localfile,remotefile = parseTCPInput(input)

fs.sendMessage(remotefile.encode()) # send filename 

reply = fs.receiveMessage() # get server's response 

if reply == "NO": # File can't be transferred 
    os.write(2,("Failed").encode())
    sys.exit(1)
        
else: # "OK"
    fd = os.open(localfile, os.O_RDONLY)
    buffer = ""
    message = ""

    while(True):
        buffer = os.read(fd,100) # read 100 bytes 
        string = buffer.decode()
        if len(string) == 0: # terminate if empty 
            break 
        message += string
        
    fs.sendMessage(message.encode()) # send the contents as a message 
    s.close()
