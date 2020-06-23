import socket
import threading

SERVER = 'https://socketserverhj.herokuapp.com/'
PORT = 2007
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

def handle_client(c, a):
    c.send(bytes("testing here btw", 'utf-8'))
    c.close()

def start():
    while True:
        c, a = server.accept()
        thread = threading.Thread(target=handle_client, args=(c, a))
        thread.start()
    
start()