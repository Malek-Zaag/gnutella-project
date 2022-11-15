from tkinter import *

# init window
root = Tk()
root.eval('tk::PlaceWindow . center')
root.geometry("750x400")
root.title("My Gnutella Client")
icon = PhotoImage(file="2.png")
root.iconphoto(True, icon)

# files
Label(root, text="Search for file here", font=("Comic Sans", 16)).grid(row=0, column=0)
entry1 = Entry(root, width=30).grid(row=0, column=1)

# clients
Label(root, text="Connected Clients", font=("Comic Sans", 16)).grid(row=0, column=3, padx=50)
listbox2 = Listbox(root, height=20, width=30).grid(row=1, column=3, padx=50)

# buttons
button1 = Button(root, text="Connect to the network", font=("comic Sans", 10)).grid(row=4, column=3)
button2 = Button(root, text="Download file", font=("Comic Sans", 10)).grid(row=4, column=0, columnspan=2, sticky="",
                                                                           pady=10)

# textarea
listbox3 = Listbox(root, height=20, width=80).grid(row=1, column=0, columnspan=3, padx=10)

root.mainloop()
