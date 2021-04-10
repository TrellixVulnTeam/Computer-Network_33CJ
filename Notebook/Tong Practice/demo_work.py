from socket import(
    socket,
    gethostname
)

s = socket()
host = gethostname()
print(host)

port = 9999
