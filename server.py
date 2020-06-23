import socket
import threading
import os

SERVER = '0.0.0.0'
PORT = os.environ['PORT']
ADDR = (SERVER, int(PORT))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(3)


def start():
    while True:
        c, a = server.accept()
        print(a)
        c.send(bytes('testing', 'utf-8'))
    
start()