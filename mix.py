import os
import socket
from tkinter import *
from tkinter import messagebox

port = 5050
my_address = socket.gethostbyname(socket.gethostname())


def check_ip():
    for i in range(100, 101):
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
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((my_address, port))
    my_socket.listen()
    check_ip()


def establish_connection(ip, filename):
    connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect_socket.connect((ip, port))
    print("conn")
    connect_socket.send(filename)
    connect_socket.close()


def search_file():
    print(2)
    filename = entry1.get()
    print(filename)
    for i in range(0, listbox2.size()):
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
