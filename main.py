# create an INET, STREAMing socket
import socket

from pyrace.client_thead import client_thread

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind(("0.0.0.0", 3000))
    # become a server socket
    serversocket.listen(5)

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        ct = client_thread(clientsocket)
        ct.run()


if __name__ == "__main__":
    main()