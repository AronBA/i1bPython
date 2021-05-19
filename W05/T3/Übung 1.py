import random


def runden(zahl):
    return round(zahl * 2) / 2


noten = []

for i in range(0, 20):
    note = random.randint(10, 60)
    note = note / 10
    noten.append(float(note))

noten.remove(min(noten))
noten.remove(max(noten))
noten = sum(noten)/len(noten)

print(runden(noten))
