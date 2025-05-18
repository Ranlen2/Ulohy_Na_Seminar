#code by Rene Cakan

from zlomek import *
import operator

class ZlomkovakaKalkulacka:
    def __init__(self):
        self.operace = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "^": operator.pow
        }

    def str2Zlomek(self, retezec):
        retezec = str(retezec)
        if "/" in retezec:
            z = retezec.split("/")
            if z[0].lstrip('-').isdigit() and z[1].lstrip('-').isdigit():
                return Zlomek(z[0], z[1])
            return None
        else:
            if retezec.lstrip('-').isdigit():
                return Zlomek(retezec, 1)
            return None

    def spustit(self):
        print("\nZadej příklad jako 'a/b + c/d'. Ukonči prázdným řádkem.")
        while True:
            vstup = input("Zadej příklad (ENTER pro ukončení): ").strip().split()
            if len(vstup) == 3:
                z1 = self.str2Zlomek(vstup[0])
                op = vstup[1]
                z2 = self.str2Zlomek(vstup[2])
                if op in self.operace:
                    zlomek3 = self.operace[op](z1, z2)
                    print(f"{z1} {op} {z2} = {zlomek3}")
                else:
                    print(f"Chyba: {op} zatím není podporovaným operátorem naší kalkulačky!")
            else:
                break

if __name__ == "__main__":
    print("\nPříklad musí mít dvě racionální čísla, jeden operátor (+, -, *, /, ^) a rovnítko.\nVšechny čtyři členy oddělte mezerami.")
    print("Operátor ^ lze také napsat pomocí klávesové zkratky ALT + 94.\nPro ukončení stiskněte ENTER.\n")
    kalk = ZlomkovakaKalkulacka()
    kalk.spustit()
