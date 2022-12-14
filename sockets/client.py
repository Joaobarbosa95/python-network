import socket

addr = "127.0.0.1"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((addr, port))

msg = str.encode("Hello from the other side")

s.send(msg)

s.close()
