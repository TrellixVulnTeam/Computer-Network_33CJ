from socket import (
    gethostname
)
import socket

host = gethostname()
port = 7777

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((host,port))

s.send(b'Hello Server')

data = s.recv(1024)
print('Received : ',repr(data))





