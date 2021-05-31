
filename = input("Gib Dateinamen ein: ")
file= open(f"{filename}.txt","w+",)

file.write('''
HERZLICH WILLKOMMEN! 
Eine Schule, zwei Abteilungen, drei Angebote. 
Wirtschaftsgymnasium 
Wirtschaftsmittelschule 
Informatikmittelschule 
''')

while True:
    userin = input("Input :")
    if userin == "q!":
        break
    else:
        file.write(f"{userin}\n")
