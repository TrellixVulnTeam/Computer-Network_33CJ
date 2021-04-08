from socket import socket,gethostname
from function.command import options

s = socket()
host = gethostname()
port = 1234

s.connect(
    (host, port)
)

MSG = s.recv(1024)
options(MSG.decode())
s.send('exit()'.encode())

while True:
    SMSG = s.recv(1024).decode()
    if SMSG.upper() == ('EXIT'):
        break
        
    options(SMSG)
    
s.close()