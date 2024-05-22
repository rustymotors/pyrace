from email.policy import HTTP
from http.server import HTTPServer
from unittest.mock import Base


class WebServer(HTTPServer):
    def __init__(self, *args):
        self.isRunning = False
        self.shutdownRequested = False
        super().__init__(*args)
    
def server_activate(self):
    self.isRunning = True
    super(self).server_activate()