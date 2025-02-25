# Programme pour calculer la somme des nombres dont le 2ème chiffre est pair
T = []  # Utilisation d'une liste au lieu de numpy pour plus de simplicité

# Saisie contrôlée de N
n = int(input("N = "))
while not (3 <= n <= 30):
    n = int(input("N = "))

# Remplissage du tableau avec validation
for i in range(n):
    while True:
        nombre = int(input(f"T[{i}] = "))
        if 100 <= nombre <= 999:
            T.append(nombre)
            break

# Calcul de la somme des nombres avec 2ème chiffre pair
somme = 0
for nombre in T:
    chiffre_central = int(str(nombre)[1])  # Récupère le 2ème chiffre
    if chiffre_central % 2 == 0:
        somme += nombre

print("Somme =", somme)