import socket
import threading
import sys
from tkinter import *

IP = '192.168.1.92'
IP2 = 'socketserverhj.herokuapp.com'
PORT = 443
HEADER_LENGTH = 1020
FORMAT = 'utf-8'

password = input("ENTER PASSWORD: ")
if password != 'HJ2007CHT':
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP2, PORT))
nickname = input("Nickname for server: ")
sock.send(bytes(nickname, 'utf-8'))

root = Tk()
root.title("Chatroom")
root.geometry("800x600")
sb = Scrollbar(root)
mylist = Listbox(root, yscrollcommand = sb.set)

def recv_data():
    while True:
        msg = sock.recv(HEADER_LENGTH).decode(FORMAT)
        mylist.insert(END, msg)

def send_data(msg):
    sock.send(bytes(msg, FORMAT))
    
thread = threading.Thread(target=recv_data)
thread.start()

mylist.pack()
mylist.place(height=400, width=700, y=0)
sb.pack( side = RIGHT )
sb.place(x=700, y=0, height=400)

def send():
    text = msg.get()
    msg.delete(0, END)
    send_data(text)
    if text == "QUIT":
        root.destroy()

msg = Entry(root)
msg.pack()
msg.place(y=500, width=700, height=50)

btn = Button(root, text="Send", command=send)
btn.pack()
btn.place(height=50, y=500, x=700, width=100)

root.mainloop()
sock.send(bytes("QUIT", FORMAT))
sock.close()
print("CLOSED")
sys.exit()