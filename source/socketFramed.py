# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This program corresponds to Lab Assignment #2. This file contains the framedSocket class which
# is used to frame messages for my tcp file transfer. 

class framedSocket:
    def __init__(self,connectedSocket):
        self.cs = connectedSocket
        self.buffer = ""

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':' # framing 
        lengthBA = bytearray(lengthStr,'utf-8')
        message = lengthBA + message
        while len(message):
            sent = self.cs.send(message) # send message
            message = message[sent:]
                    
    def receiveMessage(self):
        message = ""
        self.buffer += self.cs.recv(100).decode() # receive message
        # fix error on decoding non text
        
        left,right = partition(self.buffer) # seperate message 
        message += self.buffer[left:right] # append message
        self.buffer = self.buffer[right:] # remove message 
        
        while(self.buffer): # while there is still a message to be read 
            left,right = partition(self.buffer)
            if len(self.buffer) < right:
                self.buffer += self.cs.recv(100).decode()
            else:
                message += self.buffer[left:right]
                self.buffer = self.buffer[right:]
        return message


# This method returns the indicies of the first and last character in a message 
def partition(string):
    num =""
    while(string[0].isdigit()):
        num += string[0]
        string = string[1:]

    if num.isnumeric():
        left = len(num)+1
        right = int(num) + (len(num)+1)
        return left,right
    else:
        return None        
