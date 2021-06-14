import os
text = input("Gib ein nach was du suchst:")
dir = "../testdir"


def search(dir, text):
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            f = open(f"../testdir/{file}", "r")
            if text in f.read():
                print(f"Ich habe das gesucht in {file} gefunden")
search(dir, text)