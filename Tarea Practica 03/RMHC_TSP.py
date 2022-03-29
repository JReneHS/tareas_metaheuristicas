from itertools import permutations
import random
import numpy as np


def fitness(permutacion, distancias):
    costo = 0
    origen = np.where(permutacion == 0)
    inicio = origen
    j = 1
    n = permutacion.size
    while j < n:
        destino = np.where(permutacion == j)
        costo += distancias[origen[0], destino[0]]
        origen = destino
        j += 1
    costo += distancias[origen[0], inicio[0]]
    return costo


def permutar(ciudades):
    ciudades_mut = ciudades
    indice1 = random.randint(0, n-1)
    indice2 = random.randint(0, n-1)
    aux = ciudades_mut[indice2]
    ciudades_mut[indice2] = ciudades_mut[indice1]
    ciudades_mut[indice1] = aux

    return ciudades_mut


N = input('Ingresa el numero de evaluaciones: ')
N = int(N)

n = input('Ingresa el número de ciudades: ')
n = int(n)

distancias = np.zeros((n, n), int)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        distancias[i, j] = random.randint(1, 100)

# n se refiere al numero de ciudades
#n = 4
# ciudades=[0,1,2,3]
#distancias = [[0,16,85,12],[16,0,10,50],[85,10,0,31],[12,50,31,0]]

ciudades = np.zeros((n), int)
for i in range(n):
    ciudades[i] = i
np.random.shuffle(ciudades)

fitness_actual = fitness(ciudades, distancias)
eval = 1

print("\n")
print("Recorrido Inicial: ", ciudades)
print("con fitness igual a: ", fitness_actual[0])
print("\n")

while eval < N:
    nuevo_recorrido = permutar(ciudades)
    nueva_fitness = fitness(nuevo_recorrido, distancias)
    eval += 1

    if nueva_fitness <= fitness_actual:
        ciudades = nuevo_recorrido
        fitness_actual = nueva_fitness

print("Recorrido Final: ", ciudades)
print("con fitness igual a: ", fitness_actual[0])
