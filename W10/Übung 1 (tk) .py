import os
from tkinter import filedialog
from tkinter import *


def dir():
    dir = filedialog.askdirectory()
    return dir

def search(dir):
    text = e.get()
    for folder, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(folder, file)
                with open(path, "r") as f:
                    if text in f.read():
                        l = Label(root, text=path)
                        l.pack()

root = Tk()
e = Entry(root,bd =5)
s = Button(root, text="Search", command= lambda : search(dir()))
l1 = Label(root, text="Es wurde in folgenden Dateien gefunden:")
e.pack()
s.pack()
l1.pack()
root.mainloop()
