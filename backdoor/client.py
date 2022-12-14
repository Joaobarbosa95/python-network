import socket

HOST = "127.0.0.1"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("--> ")
    s.sendall(msg.encode())
    data = s.recv(1024)

data = data.decode("utf-8")
print(f"Received {data}")

s.close()




