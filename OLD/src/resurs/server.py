import os
import socket
import time
import threading
import UserSQL


def send(self, package):
    pass


def recive(self, package):
    pass


class Server:
    def __init__(self, host, port, user):
        self.port = port
        self.host = host
        self.user = user
        self.bufsize = 1024
        self.addr = (host, port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.addr)
        print "Server running on", host, "at port", port

        self.socket.listen(5)


def recv_loop(server, client, caddr):
    print 'Connected To', caddr

    while True:
        global clients
        name = clients[client]
        data = client.recv(1024)
        if not data:
            break
        print name + " said: " + data
    client.close()


host = 'localhost'
port = 5000
user = 'No one'

server = Server(host, port, user)

clients = {}
threads = []
while True:
    client, caddr = server.socket.accept()
    # name extraction
    name = client.recv(1024)

    clients[client] = name

    thread = threading.Thread(target=recv_loop, args=(server, client, caddr))
    thread.start()
