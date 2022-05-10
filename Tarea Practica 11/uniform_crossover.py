import random

tam_cromosoma = 10

cromosomaA = []
cromosomaB = []

for j in range(tam_cromosoma):
    cromosomaA.append(random.randint(11, 20))
    cromosomaB.append(random.randint(21, 30))

descendienteA = []
descendienteB = []
mascara_indices = []

for j in range(tam_cromosoma):
    if random.random() < 0.5:
        descendienteA.append(cromosomaA[j])
        descendienteB.append(cromosomaB[j])
        mascara_indices.append('A')
    else:
        descendienteA.append(cromosomaB[j])
        descendienteB.append(cromosomaA[j])
        mascara_indices.append('B')

print("Padre A: ", cromosomaA)
print("Padre B: ", cromosomaB)
print("Mascara: ", mascara_indices)
print("Hijo A: ", descendienteA)
print("Hijo B: ", descendienteB)
