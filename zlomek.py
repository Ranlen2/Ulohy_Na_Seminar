#code by Rene Cakan

def gcd(x, y):
    if y > x:
        x, y = y, x
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

def lcm(x, y):
    g = gcd(x, y)
    return abs(x*y//g)

class Zlomek:
    def __init__(self, citatel, jmenovatel):
        self._citatel = int(citatel)
        if jmenovatel == 0:
            print("Neplatny jemnovatel")
            exit()
        self._jmenovatel = int(jmenovatel)
        if self._jmenovatel < 0:
            self._citatel = -self._citatel
            self._jmenovatel = -self._jmenovatel

    def __add__(self, next):
        l = lcm(self._jmenovatel, next._jmenovatel)
        print(l)
        citatel_1 = (self._citatel * l // self._jmenovatel) + (next._citatel * l // next._jmenovatel)
        print(citatel_1)
        m = gcd(citatel_1, l)
        return Zlomek(citatel_1//m, l//m)

    def __sub__(self, next):
        l = lcm(self._jmenovatel, next._jmenovatel)
        citatel_1 = (self._citatel * l // self._jmenovatel) - (next._citatel * l // next._jmenovatel)
        m = gcd(citatel_1, l)
        return Zlomek(citatel_1 // m, l // m)

    def __pow__(self, next):
        return(Zlomek(int(self._citatel ** (next._citatel/next._jmenovatel)), int(self._jmenovatel ** (next._citatel/next._jmenovatel))))

    def __mul__(self, next):
        citatel_1 = self._citatel * next._citatel
        jmenovatel_1 = self._jmenovatel * next._jmenovatel
        m = gcd(citatel_1, jmenovatel_1)
        return Zlomek(citatel_1//m, jmenovatel_1//m)

    def __truediv__(self, next):
        citatel_1 = self._citatel * next._jmenovatel
        jmenovatel_1 = self._jmenovatel * next._citatel
        m = gcd(citatel_1, jmenovatel_1)
        return Zlomek(citatel_1 // m, jmenovatel_1 // m)

    def __neg__(self):
        return Zlomek(-self._citatel, self._jmenovatel)

    def __pos__(self):
        return Zlomek(self._citatel, self._jmenovatel)

    def __abs__(self):
        return Zlomek(abs(self._citatel),abs(self._jmenovatel))

    def __str__(self):
        if self._jmenovatel == 1:
            return str(self._citatel)
        return f"{self._citatel}/{self._jmenovatel}"
if __name__ == "__main__":
    z1 = Zlomek(3,4)
    z2 = Zlomek(1,3)
    z3 = z1 + z2
    print(f"{z1} + {z2} = {z3}")