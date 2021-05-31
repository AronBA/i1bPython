from random import *
lotto = set()
while len(lotto) < 6:
    num = randint(1, 50)
    lotto.add(num)
bonus = randint(1, 6)
lotto = sorted(lotto)
print(f"{lotto[0]}-{lotto[1]}-{lotto[2]}-{lotto[3]}-{lotto[4]}-{lotto[5]} ({bonus})")