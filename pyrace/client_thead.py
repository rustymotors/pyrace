
import socket


class client_thread:
    
    def __init__(self, clientsocket: socket.socket):
        self.clientsocket = clientsocket
        self.clientsocket.setblocking(False) 
    
    def run(self):
        # get a connection from client
        # clientsocket, address = clientsocket
        # print(clientsocket)
        # print(address)
        # clientsocket.send(bytes("Welcome to the server", "utf-8"))
        # clientsocket.close()
        while True:
            # get the data sent by client
            data = self.clientsocket.recv(1024)
            if not data:
                break
            print("Client sent: ", data.decode("utf-8"))
            self.clientsocket.send(data)
        self.clientsocket.close()
        print("Client disconnected")
