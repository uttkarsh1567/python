import socket

c=socket.socket()
c.connect(('localhost',9999))
a=c.recv(1024).decode()
while True:
    for _ in range(1000):
        mgs=input('enter your mgs')
        c.send(bytes(mgs,'utf-8'))
        print(c.recv(1024).decode())



