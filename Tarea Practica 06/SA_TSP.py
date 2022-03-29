from itertools import permutations
import random
import numpy as np
import math


def costo(permutacion, distancias):
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


def vecindad(ciudades):
    ciudades_mut = ciudades
    indice1 = random.randint(0, n-1)
    indice2 = random.randint(0, n-1)
    aux = ciudades_mut[indice2]
    ciudades_mut[indice2] = ciudades_mut[indice1]
    ciudades_mut[indice1] = aux

    return ciudades_mut


n = input('Ingresa el número de ciudades: ')
n = int(n)

# Generar una matriz de números aleatorios entre 1 y 100 (distancias)
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

temp_min = 0.01
temp_max = 300.0
vecinos = n - 1  # n es numero de ciudades
alfa = 0.8
K = 1.0

ciudades = np.zeros((n), int)
for i in range(n):
    ciudades[i] = i
np.random.shuffle(ciudades)

edo_anterior = costo(ciudades, distancias)

print("\n")
print("Recorrido Inicial: ", ciudades)
print("con Costo igual a: ", edo_anterior[0])
print("\n")

temp = temp_max

while temp >= temp_min:
    vecinos_revisados = 0
    while vecinos_revisados < vecinos:
        sucesor = vecindad(ciudades)
        edo_nuevo = costo(sucesor, distancias)
        delta = edo_nuevo - edo_anterior
        if delta > 0:
            if random.random() >= math.exp((-delta)/(K*temp)):
                # TODO eliminar el sucesor
                sucesor = []
                edo_nuevo = 0
            else:
                edo_anterior = edo_nuevo
                ciudades = sucesor
        else:
            edo_anterior = edo_nuevo
            ciudades = sucesor
        vecinos_revisados = vecinos_revisados + 1
        # print()
        #print("Recorrido: ", ciudades)
        #print("Costo: ", edo_anterior[0])
        #print("Temp: ", temp)
        # print()
    temp = temp * alfa


print("Recorrido Final: ", ciudades)
print("con Costo igual a: ", edo_anterior[0])
