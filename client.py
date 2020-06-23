import socket

server = 'wss://socketserverhj.herokuapp.com/0.0.0.0'
port = 2007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))

recieved = client.recv(1029).decode('utf-8')

print(recieved)