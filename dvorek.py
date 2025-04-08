#code by Rene Cakan

class Zvirata(object):
    def __init__(self, jmeno, velikost, vek):
        self._jmeno = jmeno
        self._velikost = velikost
        self._vek = vek
    def get_jmeno(self):
        return self._jmeno
    def get_velikost(self):
        return self._velikost
    def get_vek(self):
        return self._vek
    def go_to(self, lokace):
        return(f"{self._jmeno} navsitvil/a {lokace}.")
    def eat(self, jidlo):
        return(f"{self._jmeno} snedl/a {jidlo}.")

class Savci(Zvirata):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 4):
        super().__init__(jmeno, velikost, vek)
        self._pocet_nohou = pocet_nohou
    def get_pocet_nohou(self):
        return self._pocet_nohou

class Ptaci(Zvirata):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2):
        super().__init__(jmeno, velikost, vek)
        self._pocet_nohou = pocet_nohou
    def get_pocet_nohou(self):
        return self._pocet_nohou

class Pes(Savci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 4, druh = "pes", zvuk = "haf"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
        self._zvuk = zvuk
    def get_druh(self):
        return self._druh
    def get_zvuk(self):
        return(f"{self._jmeno} udelal {self._zvuk}.")

class Kocka(Savci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 4, druh = "kocka", zvuk = "mnau"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
        self._zvuk = zvuk
    def get_druh(self):
        return self._druh
    def get_zvuk(self):
        return(f"{self._jmeno} udelal {self._zvuk}.")

class Slepice(Ptaci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2, druh = "slepice", zvuk = "kotkodak"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
        self._zvuk = zvuk
    def get_druh(self):
        return self._druh
    def get_zvuk(self):
        return(f"{self._jmeno} udelal {self._zvuk}.")

class Kohout(Ptaci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2, druh = "kohout", zvuk = "kykyryky"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
        self._zvuk = zvuk
    def get_druh(self):
        return self._druh
    def get_zvuk(self):
        return(f"{self._jmeno} udelal {self._zvuk}.")

class Vrabec(Ptaci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2, druh = "vrabec", zvuk = "civi"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
        self._zvuk = zvuk
    def get_druh(self):
        return self._druh
    def get_zvuk(self):
        return(f"{self._jmeno} udelal {self._zvuk}.")

slepka1 = Slepice("Roza_1", 30, 2)
slepka2 = Slepice("Roza_2", 32, 3)
slepka3 = Slepice("Roza_3", 27, 2)
slepka4 = Slepice("Roza_4", 29, 2)
slepka5 = Slepice("Roza_5", 35, 1)
kohout = Kohout("Pepik", 50, 2)
kocka = Kocka("Micka", 45, 6)
pes = Pes("Ben", 80, 4)
sousedovic_kocka = Kocka("Picka", 44, 7)
vrabec = Vrabec("Michal", 12, 1)

print(kocka.go_to("misku"))
print(kocka.eat("vodu"))
print(pes.get_zvuk())
print(kocka.get_zvuk())
print(kocka.go_to("skrys"))



