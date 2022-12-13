import socket
import time

s = socket.socket()
s.connect(("localhost",8020))

while 1:
    msg = s.recv(1).decode()
    print("received --> ", msg)
    s.send(msg.encode())
    time.sleep(1)
