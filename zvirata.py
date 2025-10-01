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
        return(f"{self._jmeno} navsitvil {lokace}.")
    def eat(self, jidlo):
        return(f"{self._jmeno} snedl {jidlo}.")

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

class Psi(Savci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 4, druh = "Psi"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
    def get_druh(self):
        return self._druh


class Kocky(Savci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 4, druh = "Kocky"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
    def get_druh(self):
        return self._druh

class Kur(Ptaci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2, druh = "Kur"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
    def get_druh(self):
        return self._druh

class Vrabci(Ptaci):
    def __init__(self, jmeno, velikost, vek, pocet_nohou = 2, druh = "Vrabci"):
        super().__init__(jmeno, velikost, vek, pocet_nohou)
        self._druh = druh
    def get_druh(self):
        return self._druh


azor = Psi("Azor", 80, 6)
print(azor.get_jmeno())
print(azor.get_pocet_nohou())
print(azor.go_to("Ceske Budejovice"))
print(azor.eat("Salam"))
