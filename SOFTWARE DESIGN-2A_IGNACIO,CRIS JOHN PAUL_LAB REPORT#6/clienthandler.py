from codecs import decode
from threading import Thread
from datetime import datetime

BUFSIZE = 1024
CODE = "ascii"

class ClientHandler(Thread):

    def init(self, client, transcript):
        Thread.init(self)
        self.client = client
        self.transcript = transcript
    
    def currentTime(self):
            now = datetime.now()
            return now.strftime("%H:%M:%S")
    
    def run(self):
        while True:
            
            message = decode(self.client.recv(BUFSIZE), CODE)

    chunks = message.split(";;;")

    if chunks[1] == "connect":
        name = chunks[0]

        self.transcript.add(name + " - " +
        self.currentTime() + " - " +" has connected!")
        self.client.send(bytes(str(self.transcript), CODE))

    elif chunks[1] == "disconnect":
        name = chunks[0]

        self.transcript.add(name + " - " +
        self.currentTime() + " - " + "has disconnected!")
        self.client.send(bytes(str(self.transcript), CODE))
    
    elif chunks[1] == "send":

        message = chunks[0]
        self.transcript.add(name + " - " +
        self.currentTime() + " - " + message)
        self.client.send(bytes(str(self.transcript), CODE))
    
    if not message:
        print("Client disconnected")

        self.client.close() 
    