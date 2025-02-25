from numpy import * 

def saisir():
    global n
    ok = False
    while not ok:
        n = int(input("Donner un entier : "))
        ok = 3 < n < 100

def verify(ch):
    i = 0
    while i < len(ch) and ("A" <= ch[i].upper() <= "Z" or ch[i] == ' '):  # Autorise les espaces
        i += 1
    return i == len(ch)

def remplir(n):
    global tn, tm
    tn = array([str] * n)
    tm = array([float] * n)
    for i in range(n):
        ok = False
        while not ok:
            tn[i] = input(f"Donner tn[{i}] = ")
            ok = verify(tn[i])
        ok = False
        while not ok:
            tm[i] = float(input("Donner la moyenne : "))
            ok = 0 <= tm[i] <= 20

def tri(n, tn, tm):
    for i in range(n-1):
        pos_max = i
        for j in range(i+1, n):
            if tm[pos_max] < tm[j]:
                pos_max = j
        if i != pos_max:
            # Échange des moyennes (tm)
            tm[i], tm[pos_max] = tm[pos_max], tm[i]
            # Échange des noms (tn)
            tn[i], tn[pos_max] = tn[pos_max], tn[i]

def afficher(n, tn, tm):
    for i in range(n):
        if tm[i] >= 10:
            print(f"{tn[i]} : {tm[i]}")

# Exécution principale
saisir()
remplir(n)
tri(n, tn, tm)
afficher(n, tn, tm)