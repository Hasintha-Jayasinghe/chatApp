import socket
import threading
import os

IP = ''
PORT = 2007
FORMAT = 'utf-8'
HEADER_LENGTH = 1020
print(PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, int(PORT)))
server.listen()

connected_user_names = []
connected_addrs = []

def handler(conn, a):
    nickname = conn.recv(HEADER_LENGTH).decode(FORMAT)
    connected_user_names.append(nickname)
    connected_addrs.append(conn)
    for c in connected_addrs:
        c.send(bytes(f"{nickname} joined the chat. There are {len(connected_user_names)} people in the chat now", FORMAT))
        print(f"{nickname} joined the chat. There are {len(connected_user_names)} people in the chat now")
    connected = True
    while connected:
        try:
            msg = conn.recv(HEADER_LENGTH).decode(FORMAT)

            for c in connected_addrs:
                c.send(bytes(nickname + ": " + msg, FORMAT))
            
            if msg == 'QUIT':
                connected_user_names.remove(nickname)
                connected_addrs.remove(conn)
                connected = False
        except Exception as e:
            print("ERROR")
            print(e)
            conn.close()
    
    conn.close()

def start():
    print("STARTING SERVER ON IP/HOST: " + IP)
    while True:
        conn, a = server.accept()
        thread = threading.Thread(target=handler, args=(conn, a))
        thread.start()

start()