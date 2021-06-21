import csv
input = int(input("Wähle reihe"))

with open("data.csv") as f:
    data = csv.reader(f, delimiter=";")

    if input !=0:
        for row in data:
            print(row)

    else:
        for row in data:
            print(row)



