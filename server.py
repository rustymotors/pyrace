from os import name
from typing import Any, Dict
from twisted.internet import selectreactor
from twisted.internet.defer import Deferred
from twisted.internet.interfaces import IListeningPort, IReactorCore
from twisted.internet.protocol import Protocol, Factory
selectreactor.install()
from twisted.internet import reactor, endpoints

class ServerEntry:
    def __init__(self, reactor: Any, name: str, port: int, protocol: type[Protocol]):
        self.name = name
        self.port = port
        self.protocol = protocol
        self.endpoint = endpoints.serverFromString(reactor, f"tcp:{port}").listen(Factory.forProtocol(protocol))
        self.endpoint.addCallback(self.onListen)
        self.endpoint.addErrback(self.onError)
        
    def onListen(self, port: IListeningPort):
        print(f"Server {self.name} is listening on port {port.getHost().port}")
        
    def onError(self, error):
        print(f"Error starting server {self.name}: {error}")

class NPSProtocol(Protocol):
    
    def __init__(self):
        pass
    
    def connectionMade(self):
        print("Connection made")
        
    def dataReceived(self, data):
        print("Data received")
        print(data)
        
    def connectionLost(self, reason):
        print("Connection lost")

def main():
    
    servers: Dict[str, ServerEntry] = {}
    
    servers["Login"] = ServerEntry(reactor, "Login", 8226, NPSProtocol)
    servers["Persona"] = ServerEntry(reactor, "Persona", 8228, NPSProtocol)
    servers["Lobby"] = ServerEntry(reactor, "Lobby", 7003, NPSProtocol)
        
    reactor.run() # type: ignore
    
if __name__ == "__main__":
    main()
