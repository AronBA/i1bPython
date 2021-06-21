import os
from tkinter import *
dir = "../testdir"

def search(dir):
    text = e.get()
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            f = open(f"../testdir/{file}", "r")
            if text in f.read():
                print(f"Ich hab es gefunden in {file}")
                global l
                l = Label(root, text=file)
                l.pack()





text = "hello"

root = Tk()
e = Entry(root,bd =5)
s = Button(root, text="Search", command= lambda : search(dir))
l1 = Label(root, text="Es wurde in folgenden Dateien gefunden:")

e.pack()
s.pack()
l1.pack()


root.mainloop()
