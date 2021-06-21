import os
from tkinter import *
dir = "../testdir"

def search(dir, text):
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            f = open(f"../testdir/{file}", "r")
            if text in f.read():
                print(f"Ich habe das gesucht in {file} gefunden")




text = "hello"

root = Tk()
e = Entry(root)
s = Button(root, text="Search", command= lambda : search(dir, text))
e.pack()
s.pack()
root.mainloop()
