import os
import socket

port = 5050
my_address = socket.gethostbyname(socket.gethostname())
print(my_address)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((my_address, port))
my_socket.listen()


def handle_client(conn, addr):
    print(addr + " online")
    connected = True
    print("here2")
    while connected:
        msg = conn.recv()
        print(msg)


# conn, addr = my_socket.accept()
# thread = threading.Thread(target=handle_client, args=(conn, addr))
while True:
    for i in range(100, 101):
        hostname = my_address[:-1] + str(i)
        print(hostname)
        response = os.system(f"ping -n 1 {hostname}")
        if response == 0:
            print("here1")
        else:
            print(hostname + " offline")
