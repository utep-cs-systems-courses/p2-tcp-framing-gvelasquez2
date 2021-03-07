# Gilbert Velasquez
# CS 4375: Theory of Operating Systems
# Dr. Freudenthal
# This program corresponds to Lab Assignment #2.

class framedSocket:
    def __init__(self,connectedSocket):
        self.cs = connectedSocket

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':'
        lengthBA = bytearray(lengthStr,'utf-8')
        message = lengthBA + message
        self.cs.send(message)

        
    def receiveMessage(self):
        message = ""
        data = self.cs.recv(100).decode()
        left,right = partition(data)
        message += data[left:right]
        data = data[right:]
        
        while(data):
            left,right = partition(data)
            if len(data) < right:
                data += self.cs.recv(100).decode()
            else:
                message += data[left:right]
                data = data[right:]
        return message
        

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

def parse(string):
    left,right = partition(string)

    if len(string) < right:
        return None,string
    else:
        message = string[left:right]
        remainingString = string[right:]

        if remainingString == "":
            return message,remainingString
        else:
            return message,remainingString


        
