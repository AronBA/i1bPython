class Übung:
    def __init__(self):
        self.a = [1, 1, 2, 3, 5, 8, 12, 21, 34, 55, 89]

    def aufgabe(self):
        for i in self.a:
            if i < 5:
                print(i)

    def extra(self):
        a = self.a
        b = []
        for i in a:
            if i < 5:
                b.append(i)
        print(b)

u = Übung()
u.aufgabe()
u.extra2()
