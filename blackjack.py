#code by Rene Cakan

import random

class Karta(object):

    SEZNAM_BAREV = {"T","P","K","S"}
    BARVA_MAP = { "T":"♣", "P":"♠", "S":"♥", "K":"♦"}
    SEZNAM_HODNOT = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"}
    SEZNAM_VAH = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

    def __init__(self,barva, hodnota):
        self._barva = None
        self._hodnota = None
        if barva in Karta.SEZNAM_BAREV:
            self._barva = barva
        if hodnota in Karta.SEZNAM_HODNOT:
            self._hodnota = hodnota

    def __str__(self):
        return Karta.BARVA_MAP[self._barva] + self._hodnota

    def zobraz(self):
        print(str(self) , end = ' ')

    def get_vaha(self):
        return Karta.SEZNAM_VAH[self._hodnota]

    def eso(self):
        return self._hodnota == "A"

class Hrac(object):
    def __init__(self, name):
        self._name = name
        self._hand = []

    def pridej(self,karta):
        self._hand.append(karta)

    def secti(self):
        soucet = 0
        esa = 0
        for i in self._hand:
            soucet += i.get_vaha()
            if i.eso():
                esa += 1
        if esa == 0:
            return soucet
        else:
            while esa > 0 and soucet > 21:
                soucet -= 10
                esa -= 1
            return soucet

    def get_name(self):
        return self._name

    def show(self):
        print (f"> {self._name}\n-------------")
        for karta in self._hand:
            karta.zobraz()
        print(f"\nSoucet: {self.secti()}")
        print ("-------------")

class Balicek(object):
    def __init__(self):
        self._deck = []
        for barva in Karta.SEZNAM_BAREV:
            for hodnota in Karta.SEZNAM_HODNOT:
                karta = Karta(barva, hodnota)
                self._deck.append(karta)

    def zamichat(self):
        random.shuffle(self._deck)

    def sejmi(self):
        return self._deck.pop()

class Game(object):
    print("Cilem hry je dostat se co nejblize 21, ale tuto hranici nepresahnout.")
    def __init__(self):
        self._balicek = Balicek()
        self._balicek.zamichat()
        self._hrac = Hrac("Hrac")
        self._pocitac = Hrac("Pocitac")

    def run(self):
        for _ in range(2):
            self._hrac.pridej(self._balicek.sejmi())
            self._pocitac.pridej(self._balicek.sejmi())
        while True:
            self._hrac.show()
            if self._hrac.secti() > 21:
                break
            akce = input("Chceš další kartu(1=ANO,0=NE)?: ")
            if akce.lower() != '1':
                break
            self._hrac.pridej(self._balicek.sejmi())
        while self._pocitac.secti() < 17:
            self._pocitac.pridej(self._balicek.sejmi())
        hrac_score = self._hrac.secti()
        pocitac_score = self._pocitac.secti()
        if hrac_score == pocitac_score or hrac_score > 21 and pocitac_score > 21:
            print("Remizoval jsi.")
        elif hrac_score <= 21 and (pocitac_score > 21 or pocitac_score < hrac_score):
            print("Vyhral jsi")
        else:
            print("Prohral jsi")

Game().run()
