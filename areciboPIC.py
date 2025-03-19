#code by Rene Cakan
import random
def pbm(a):
    with open("arecibo10.pbm", "w") as vystup:
        sirka = len(a[0]) * 10
        vyska = len(a) * 10
        vystup.write(f"P1\n{sirka} {vyska}\n")
        for row in a:
            for _ in range(10):
                vystup.write(" ".join((char + " ") * 10 for char in row) + "\n")
def ppm(a):
    with open("arecibo.ppm", "w") as vystup:
        sirka = len(a[0]) * 10
        vyska = len(a) * 10
        vystup.write(f"P3\n{sirka} {vyska}\n255\n")
        for row in a:
            for _ in range(10):
                vystup.write(" ".join([("0 0 0 " * 10) if char == '0' else (" ".join([str(random.randint(0, 255)) for _ in range(3)]) + " ") * 10 for char in row]) + "\n")
with open(r"D:\input.txt", "r") as vstup:
    arecibo = []
    for i in vstup:
        arecibo.append(i.strip())
    pbm(arecibo)
    ppm(arecibo)