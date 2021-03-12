# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This program corresponds to Lab Assignment #2. This file contains the framedSocket class which
# is used to frame messages for my tcp file transfer. 

class framedSocket:
    def __init__(self,connectedSocket):
        self.cs = connectedSocket

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':' # framing 
        lengthBA = bytearray(lengthStr,'utf-8')
        message = lengthBA + message
        self.cs.send(message) # send message 

        
    def receiveMessage(self):
        message = ""
        data = self.cs.recv(100).decode() # receive message 
        left,right = partition(data) # seperate message 
        message += data[left:right] # append message
        data = data[right:] # remove message 
        
        while(data): # while there is still a message to be read 
            left,right = partition(data)
            if len(data) < right:
                data += self.cs.recv(100).decode()
            else:
                message += data[left:right]
                data = data[right:]
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
