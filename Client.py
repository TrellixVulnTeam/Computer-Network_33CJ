
from socket import socket, gethostname

from function.connect import ask_port
from function.client_function import *


def connect(s):
    s.connect(
        (host, port)
    )


s = socket()
host = gethostname()
port = ask_port()
login_status = False

try:
    system("cls")
    connect(s)
    user = login(s)
    login_status = insert_login_logs(user)

    while True:
        status = workflow(s, user)
        if status == 'break':
            break
        else:
            s.send("exit".encode())

except ConnectionResetError:
    line_break("Exiting...")
    sleep(2)
    system("cls")
    line_break("Thank you!!")


except ConnectionRefusedError:
    line_break("Server was closed.")

except EOFError:
    line_break("Server not sending anything!!")

finally:
    if login_status:
        update_logout_logs(user)

