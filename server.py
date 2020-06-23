import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 10293
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(c, a):
    c.send("testing here btw")
    c.close()

def start():
    while True:
        c, a = server.accept()
        thread = threading.Thread(target=handle_client, args=(c, a))
        thread.start()