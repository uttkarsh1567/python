import socket

s=socket.socket()
s.bind(('localhost',9999))
print("socket created")
s.listen(100)
print("waiting for connection")

while True:
    c,add=s.accept()
    print("connected with",add)
    c.send(bytes('welcome to  chat bot','utf-8'))
    for _ in range(1000):
        mgs=c.recv(1024).decode()
        print(mgs)
        servermgs=input('enter mgs')
        c.send(bytes(servermgs,'utf-8'))