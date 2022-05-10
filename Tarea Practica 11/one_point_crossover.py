import random

tam_cromosoma = 10

cromosomaA = []
cromosomaB = []

for j in range(tam_cromosoma):
    cromosomaA.append(random.randint(0, 1))
    cromosomaB.append(random.randint(0, 1))

punto_corte = random.randint(1, tam_cromosoma-1)

descendienteA = cromosomaA[:punto_corte] + cromosomaB[punto_corte:]
descendienteB = cromosomaB[:punto_corte] + cromosomaA[punto_corte:]

print("Padre A: ", cromosomaA)
print("Padre B: ", cromosomaB)
print("Punto de corte:", punto_corte)
print("Hijo A: ", descendienteA)
print("Hijo B: ", descendienteB)
