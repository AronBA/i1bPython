L = ['Meier', 'Madasd', 'Momo', 'Molitor', 'Martin', "Mama"]
Buchstabe = input("Gib deinen Buchstaben an")
count = 0
for i in L:
    if i[0] == Buchstabe:
        count += 1

if count == len(L):
    print(f"yes, all {Buchstabe} dudes")
else:
    print(f"no, not all {Buchstabe} dudes")
