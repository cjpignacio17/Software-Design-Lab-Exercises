from socket import *
from clienthandler import ClientHandler
from threadsafetranscript import ThreadSafeTranscript

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

transcript = ThreadSafeTranscript()

while True:
    
    print("Waiting for connection . . .")

    client, address = server.accept()
    print("... connected from: ", address)
    handler = ClientHandler(client, transcript)
    handler.start()

    class Transcript:
    
        def init(self):

            self.fullTranscript = []
    
        def __str__(self):
        
            return "\n".join(self.fullTranscript)

        def add(self, message):

            self.fullTranscript.append(message)