# GIlbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Fruedenthal
# This program ...

from os import read

next = 0
limit = 0

# This method calls read to filla buffer, and gets one character at a time
def my_getChar():
    global next
    global limit

    if next == limit:
        next = 0
        limit = read(0,100)

        if limit == 0:
            return None

    if next < len(limit) -1: # Check to make sure limit[next] wont go out of bounds 
        c = chr(limit[next]) # Convert from ascii to character 
        next +=1
        return c
    else:
        return None

# This method returns the line obtained from file descriptor 0 as a String.    
def my_getLine():
    global next
    global limit
    line = ""
    char = my_getChar()
    while(char != '' and char != None):
        line += char
        char = my_getChar()
    next = 0
    limit = 0
    return line

# This method spilts a string into the seperate arguments. To be used in TCP file transfer lab
def parseTCPInput(string):
    tokens = string.split()
    command = tokens[0]
    localfile = tokens[1]
    tokens2 = tokens[2].split(':')
    host = tokens2[0]
    remotefile = tokens2[1]

    return command,localfile,host,remotefile
