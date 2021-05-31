
filename = input("Gib Dateinamen ein: ")
file= open(f"{filename}.txt","w+",)

file.write('''
HERZLICH WILLKOMMEN! 
Eine Schule, zwei Abteilungen, drei Angebote. 
Wirtschaftsgymnasium 
Wirtschaftsmittelschule 
Informatikmittelschule 
''')


istrue = True
while istrue:
    userin = input("Input :")
    if userin == "q!":
        istrue = False
    else:
        file.write(f"{userin}\n")




