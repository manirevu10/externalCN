import socket
import random 
import time

s = socket.socket()
s.bind(("localhost",8020))
s.listen(5)
c, adr = s.accept()

noframes = int(input())
windsize = int(input())

start = 0
end = 0
frame = 0

for i in range(windsize):
    print("sending --> ", frame)
    c.send(str(frame).encode())
    frame += 1
    end += 1
    time.sleep(1)

while start < noframes:
    msg = int(c.recv(1).decode())
    if start != msg:
        continue
    
    if random.randint(1, 7) < 5:
        print("acknowledgement received")
        if frame < noframes:
            print("sending -->", frame)
            c.send(str(frame).encode())
            frame += 1
            end += 1
        start += 1
        time.sleep(1)
    else:
        print("acknowledgement not received -- timeout")
        frame = start
        for _ in range(start, end):
            print("sending again --> ",frame)
            c.send(str(frame).encode())
            frame += 1
            time.sleep(1)
