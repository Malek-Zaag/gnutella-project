import os
import socket
import threading
from tkinter import *
from tkinter import messagebox

import tqdm as tqdm

# general port in use
port = 5050
# determine my address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_address = s.getsockname()[0]
print(s.getsockname()[0])
s.close()


# server listening
def server_listen():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((my_address, port))
    my_socket.listen()
    conn, addr = my_socket.accept()
    filename = conn.recv(1024).decode()
    print(filename)
    try:
        if os.path.isfile("./data/test.txt"):
            file = open(filename, "rb")
            data = file.read()
            conn.send(filename.encode())
            conn.send(os.path.getsize(filename))
            
            conn.sendall(data)
            file.close()
            conn.close()
        else:
            pass
    except FileNotFoundError:
        print("File Not Found")
        conn.close()


def check_ip():
    for i in range(140, 141):
        third_point = my_address.index(".", 8, None)
        hostname = my_address[:third_point + 1] + str(i)
        response = os.system(f"ping -n 1 {hostname}")
        print(hostname)
        if response == 0:
            print(hostname + "is online")
            listbox2.insert(i, hostname)
        else:
            print(hostname + " is offline")
    messagebox.showinfo("Connected", "You successfully connected to network")


def add_ip():
    listbox2.insert(1, my_address)
    threading.Thread(target=server_listen, args=()).start()
    check_ip()


def establish_connection(ip, filename):
    connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect_socket.connect((ip, port))
    print("conn")
    filename = filename.encode()
    connect_socket.send(filename)
    if connect_socket.recv(1024).decode() == filename:
        print("filename found")
        file_size = connect_socket.recv(1024).decode()
        listbox3.insert(0, "file found in ", ip, " client")
        connect_socket.recv(1024)
        file = open("./data/" + filename, "wb")
        file_bytes = b""
        done = False
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))
        while not done:
            data = connect_socket.recv(1024)
            if file_bytes[-5:] == b"<END>":
                done = True
            else:
                file_bytes += data
            progress.update(1024)
        file.write(file_bytes)
    connect_socket.close()


def search_file():
    print(2)
    filename = entry1.get()
    print(filename)
    for i in range(1, listbox2.size()):
        print(listbox2.get(i))
        establish_connection(listbox2.get(i), filename)


# init window
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry("750x400")
root.title("My Gnutella Client")
icon = PhotoImage(file="2.png")
root.iconphoto(True, icon)

# files
Label(root, text="Search for file here", font=("Comic Sans", 16)).grid(row=0, column=0)
entry1 = Entry(root, width=30)
entry1.grid(row=0, column=1)
button3 = Button(root, text="Search", font=("Comic Sans", 10), command=search_file)
button3.grid(row=0, column=2)

# clients
Label(root, text="Connected Clients", font=("Comic Sans", 16)).grid(row=0, column=3, padx=50)
listbox2 = Listbox(root, height=20, width=30)
listbox2.grid(row=1, column=3, padx=50)

# buttons
button1 = Button(root, text="Connect to the network", font=("comic Sans", 10), command=add_ip)
button1.grid(row=4, column=3)
button2 = Button(root, text="Download file", font=("Comic Sans", 10))
button2.grid(row=4, column=0, columnspan=2, sticky="", pady=10)

# textarea
listbox3 = Listbox(root, height=20, width=80)
listbox3.grid(row=1, column=0, columnspan=3, padx=10)
root.mainloop()
