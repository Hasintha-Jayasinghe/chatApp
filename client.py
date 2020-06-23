import socket

server = '172.17.140.46'
port = 43908

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))

recieved = client.recv(1029).decode('utf-8')

print(recieved)