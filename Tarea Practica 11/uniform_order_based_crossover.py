import random
import numpy as np


tam_cromosoma = 10

# Inicializacion de cromosomas Padres
cromosomaA = np.zeros((tam_cromosoma), int)
cromosomaB = np.zeros((tam_cromosoma), int)

# Damos Valores a cromosomas Padres
for i in range(tam_cromosoma):
    cromosomaA[i] = i+1
    cromosomaB[i] = i+1
# Revolvemos cromosomas Padres de forma aleatoria
np.random.shuffle(cromosomaA)
np.random.shuffle(cromosomaB)

# Inicializacion Plantilla binaria aleatoria
template_binario = np.zeros((tam_cromosoma), int)
# Rellenamos Plantilla binaria aleatoria
for i in range(tam_cromosoma):
    template_binario[i] = random.randint(0, 1)

# Inicializacion de cromosomas Hijos
descendienteA = np.zeros((tam_cromosoma), int)
descendienteB = np.zeros((tam_cromosoma), int)

# Rellenamos Hijos con Plantilla binaria aleatoria
for i in range(tam_cromosoma):
    if template_binario[i] == 1:
        descendienteA[i] = cromosomaA[i]
        descendienteB[i] = cromosomaB[i]


buffer_hijo_A = []
buffer_hijo_B = []

# creando Buffer de genes restantes del Hijo A
for i in range(tam_cromosoma):
    if not (cromosomaB[i] in descendienteA):
        buffer_hijo_A.append(cromosomaB[i])

# creando Buffer de genes restantes del Hijo B
for i in range(tam_cromosoma):
    if not (cromosomaA[i] in descendienteB):
        buffer_hijo_B.append(cromosomaA[i])


# Rellenar los espacios restantes del Hijo A con los valores en orden del Padre B
padre = 0
for i in range(tam_cromosoma):
    if descendienteA[i] == 0:
        descendienteA[i] = buffer_hijo_A[padre]
        padre += 1


# Rellenar los espacios restantes del Hijo B con los valores en orden del Padre A
padre = 0
for i in range(tam_cromosoma):
    if descendienteB[i] == 0:
        descendienteB[i] = buffer_hijo_B[padre]
        padre += 1


print("Padre A: ", cromosomaA)
print("Padre B: ", cromosomaB)
print("Plantilla: ", template_binario)
print("Hijo A: ", descendienteA)
print("Hijo B: ", descendienteB)
