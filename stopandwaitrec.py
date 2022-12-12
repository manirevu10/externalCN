import socket
import time

s = socket.socket()
s.connect(("localhost",8020))
while 1:
    msg = s.recv(1).decode()
    print("recived --> ", msg)
    s.send(str(int(msg) ^ 1).encode())
    time.sleep(1)
