#code by Rene Cakan
from collections import defaultdict

with open(r"D:\zaci.txt", "r") as vstup:
    d = defaultdict(int)
    nejdelsi_jmeno = []
    nejdelsi_jmeno_counter = 0
    nejcastejsi_jmeno = ""
    nejcastejsi_jmeno_counter = 0
    for i in vstup:
        x = i.split()
        if(len(x) > nejdelsi_jmeno_counter):
            nejdelsi_jmeno_counter = len(x)
            nejdelsi_jmeno = [j for j in x]
        for j in range(len(x)):
            if j == len(x) - 1:
                x[j] = '-' + x[j] + '-'
            else:
                d[x[j]] += 1
                x[j] = '*' + x[j] + '*'
        print(*x)
    for i, x in d.items():
        if x > nejcastejsi_jmeno_counter:
            nejcastejsi_jmeno_counter = x
            nejcastejsi_jmeno = i
    print("Nejcastejsi jmeno je:", nejcastejsi_jmeno)
    print("Nejdelsi jemno je:", *nejdelsi_jmeno)
