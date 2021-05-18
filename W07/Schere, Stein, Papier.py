import random
choices = ["stein","papier","schere"]
botcount = 0
usercount = 0
end = True
name = True
while name:
    try:
        länge = int(input("wähle anzahl runden: "))
        name = False

    except ValueError:
        print("use a number")


def abfrage():
    if botcount == länge or usercount == länge:
        global end
        end = False


while end:
    bot = random.choice(choices)
    user = input("wähle stein, papier, schere")
    if user in choices:
        if bot == user:
            print("unentschieden")
        else:
            if user == choices[0]:
                if bot == choices[2]:
                    print(f"Du hast gewonnen, ich hatte {bot}")
                    usercount += 1
                    abfrage()
                else:
                    print(f"Du hast verloren, ich hatte {bot}")
                    botcount += 1
                    abfrage()
            elif user == choices[1]:
                if bot == choices[0]:
                    print(f"Du hast gewonnen, ich hatte {bot}")
                    usercount += 1
                    abfrage()
                else:
                    print(f"Du hast verloren, ich hatte {bot}")
                    botcount += 1
                    abfrage()
            elif user == choices[2]:
                if bot == choices[1]:
                    print(f"Du hast gewonnen, ich hatte {bot}")
                    usercount += 1
                    abfrage()
                else:
                    print(f"Du hast verloren, ich hatte {bot}")
                    botcount += 1
                    abfrage()

    else:
        print("ungültige antwort")


if botcount > usercount:
    print('''------------------
the bot has won
-------------------''')
else:
    print('''------------------
the player has won
-------------------''')