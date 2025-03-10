#code by Rene Cakan

with open(r"D:\vstup.dat", "r") as vstup:
    soustava = int(vstup.readline())
    cislo = int(vstup.readline())
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    zaporny = False
    if cislo < 0:
        zaporny = True
        cislo = abs(cislo)
    odpoved = ""
    while cislo > 0:
        odpoved = znaky[cislo % soustava] + odpoved
        cislo //= soustava
    if zaporny:
        odpoved = '-' + odpoved
    print(odpoved)