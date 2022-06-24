from socket import *
from clienthandler import ClientHandler
from threadsafetranscript import ThreadSafeTranscript

class ThreadSafeTranscript:
    
    def __init__(self):

        transcript = Transcript()
        
    self.cell = SharedCell(transcript)

    def __str__(self):
        return self.cell.read(lambda transcript: str(transcript))

    def add(self, message):
        return self.cell.read(lambda transcript: transcript.add(message))