"""
Renkame tanko judejimo kryptį įvestimi.
Srenkamies šauti ar ne.
Gauname informaciją apie tanko koordinates ir atliktų šūvių nurodytomis kryptimis skaičių.
Paklausimas ar tęsti žaidimą.
"""


class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "s", "p", "v", "r"
        self.siaure = 0
        self.pietus = 0
        self.vakarai = 0
        self.rytai = 0
        self.s_suma = 0

    def judeti(self, kryp):

        if kryp == "s":
            self.y += 1

        elif kryp == "p":
            self.y -= 1

        if kryp == "v":
            self.x -= 1

        elif kryp == "r":
            self.x += 1

    def sauti(self, kryp):
        if kryp == "s":
            self.siaure += 1
            print("Šovė į Šiaurę.")

        elif kryp == "p":
            self.pietus += 1
            print("Šovė į Pietus.")

        if kryp == "v":
            self.vakarai += 1
            print("Šovė į Vakarus")

        elif kryp == "r":
            self.rytai += 1
            print("Šovė į Rytus")

        self.s_suma += 1

    def informacija(self):
        print("Tanko koordinatės: x ", naujas_t.x, "y", naujas_t.y)
        print("Šiaure: " + f"{self.siaure}")
        print("Pietus: " + f"{self.pietus}")
        print("Vakarai: " + f"{self.vakarai}")
        print("Rytai: " + f"{self.rytai}")
        print("Šauta šūvių is viso: " + f"{self.s_suma}")


naujas_t = Tankas()

while True:

    kryp = input("Įveskite kryptį (s, p, v, r): ")

    naujas_t.judeti(kryp)

    saud = input("Ar sauti? (t = taip/n = ne): ")
    if saud == "t":
        naujas_t.sauti(kryp)

    naujas_t.informacija()

    paklausimas = input("Ar baigti žaidimą (y = Taip, enter = testi): ")
    if paklausimas == "y":
        break

print("Viso gero!")
