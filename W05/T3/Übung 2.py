
def umrechnungkelvin(von, zahl):
    if von == 1:
        zahl += 273.15
        k = zahl
        return k

    elif von == 2:
        zahl = 5/9 * (zahl - 32)
        zahl += 273.15
        k = zahl
        return k

    elif von == 3:
        k = zahl
        return k

von = int(input('''Gib den Typ deines Wertes an
-----------------------------------
[1] Celsius
[2] Fahrenheit
[3] Kelvin
-----------------------------------
                        '''))
zahl = int(input("Gib deinen Wert ein"))

nach = int(input('''Gin den Typ in welcher dein Wertes umgerechnet werden soll
-----------------------------------
[1] Celsius
[2] Fahrenheit
[3] Kelvin
-----------------------------------
                        '''))

if nach == 1:
    k = umrechnungkelvin(von, zahl)
    k -= 273.15
    print(k)

elif nach == 2:
    k = umrechnungkelvin(von, zahl)
    k -= 273.15
    k = (k * 9/5) + 32
    print(k)
elif nach == 3:

    print(umrechnungkelvin(von, zahl))



