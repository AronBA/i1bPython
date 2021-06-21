import os
file = input("Choose you file: ")
newname = input("choose new name:")
os.rename(f"../testdir/{file}", f"../testdir/{newname}")