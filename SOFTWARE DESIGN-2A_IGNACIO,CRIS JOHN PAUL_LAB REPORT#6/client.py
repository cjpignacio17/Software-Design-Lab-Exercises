from socket import *
from codecs import decode
from unicodedata import name
from breezypythongui import EasyFrame

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

class Client(EasyFrame):
    COLOR = "#CCEEFF"

def init(self):

    EasyFrame.init(self, title = "Chat Room", background = Client.COLOR)

    self.nameLabel = self.addLabel(row = 0, column = 0,
                                   sticky = "E",
                                   text = "Enter your name: ")
    self.nameField = self.addTextField(row = 0, column = 1,
                                    text = "")
    self.connectButton = self.addButton(row = 0, column = 2,
                                    text = "Connect",
                                    command = self.connect)
    self.messageField = self.addTextField(row = 1, column = 0,
                                    text = "", sticky = "NSEW",
                                    columnspan = 2)
    self.sendButton = self.addButton(row = 1, column = 2,
                                    text = "Send message",
                                    command = self.send)
    self.chatArea = self.addTextArea(row = 2, column = 0,
                                     text = "", columnspan = 3,
                                     width = 50)

def connect(self):

    self.server = socket(AF_INET, SOCK_STREAM)
    self.server.connect(ADDRESS)
    name = self.nameField.getText()
    self.server.send(bytes(name + ";;;connect", CODE))
    transcript = decode(self.server.recv(BUFSIZE), CODE)
    self.chatArea.setText(transcript)
    self.connectButton["text"] = "Disconnect"
    self.connectButton["command"] = self.disconnect

def disconnect(self):
    name = self.nameField.getText()
    self.server.send(bytes(name + ";;;disconnect", CODE))
    self.messageBox(message = "User is disconnected.")
    self.connectButton["text"] = "Connect"
    self.connectButton["command"] = self.connect
    self.chatArea.setText("")
    self.server.close()

def send(self):
    message = self.messageField.getText()
    self.server.send(bytes(message + ";;;send", CODE))
    transcript = decode(self.server.recv(BUFSIZE), CODE)
    self.chatArea.setText(transcript)
    self.messageField.setText("")
    
def main():

    Client().mainloop()

if name == "main":
    
    main()
