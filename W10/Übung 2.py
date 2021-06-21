import csv
data = "data.csv"
input = int(input("Welche Zeile möchtest du sehen?"))
fields = []
rows = []

with open(data, "r") as data:
    data = csv.reader(data)
    fields = next(data)
    for row in data:
        rows.append(row)

if input != 0:
    for row in rows[input]:
        for col in row:
            print(col),
    print('\n')
else:
    for row in rows:
        for col in row:
            print("%10s" % col),
    print('\n')
