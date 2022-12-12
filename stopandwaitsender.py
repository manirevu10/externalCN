import socket
import random
import time

s = socket.socket()
s.bind(("localhost",8020))
s.listen(5)
c, adr = s.accept()
a = int(input())
x = 0
print("sending --> ", x)
c.send(str(x).encode())
while a > 0:
    time.sleep(2)
    recv = c.recv(1).decode()
    if random.randint(1,7) <= 5:
        x ^= 1
        print("acknowledgement recivied")
        print("Sending --> ",x)
        c.send(str(x).encode())
        a -= 1 
    else:
        print("acknowledgement not recivied")
        print("sending again -->", x)
        c.send(str(x).encode())


    
