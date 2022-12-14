import socket
addr = "127.0.0.1"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr, port))

''' 1 connections allowed'''
s.listen(1) 

print("Server started")

connection, address = s.accept()

while 1:
    data = connection.recv(1024)
    if not data: break
    print(data.decode("utf-8"))

connection.close()



