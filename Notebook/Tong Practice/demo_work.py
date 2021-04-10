from socket import(
    socket,
    gethostname
)

s = socket()
host = gethostname()
print(host)

port = 9999
s.bind((host,port))
s.listen()

while True:
    c, addr = accept()
    print('Connection From : ',addr)


