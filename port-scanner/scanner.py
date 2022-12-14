import socket

target = "127.0.0.1"

low_port = 1
high_port = 1024

for port in range(low_port, high_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print(f"-- Port {port} open --")
    else: 
        print(f"-- Port {port} closed --")

    s.close()

