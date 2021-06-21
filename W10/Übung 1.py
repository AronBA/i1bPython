import os

def search(dir, text):
    for folder, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(folder, file)
                with open(path, "r") as f:
                    if text in f.read():
                        print(f"Text wurde in {path} gefunden")


userinput = input("Was suchst du: ")
path = "../testdir"
search(path, userinput)
