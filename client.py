import socket

#server = '172.17.140.46'
server = 'socketserverhj.herokuapp.com'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))

recieved = client.recv(102900).decode('utf-8')

print(recieved)