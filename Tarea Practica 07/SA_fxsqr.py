import copy
import random
import math

def costo(funcion):
    valmax = 0
    for i in funcion:
        valmax += i**2
    return valmax


def vecindad(funcion,n):
    new_funcion = funcion.copy()
    locus = random.randint(0, n-1)
    new_funcion[locus] = random.uniform(-10, 10)
    return new_funcion

n = input('Ingresa el número de elementos: ')
n = int(n)

funcion_x = []
for i in range(n):
    funcion_x.append(random.uniform(-10, 10))

temp_min = 0.01
temp_max = 300.0
vecinos = n - 1  # n es numero de elementos en el arreglo
alfa = 0.8
K = 1.0

edo_anterior = costo(funcion_x)

print("\n")
print("Valores Iniciales: ", funcion_x)
print("costo igual a: ", edo_anterior)
print("\n")

temp = temp_max

while temp >= temp_min:
    vecinos_revisados = 0
    while vecinos_revisados < vecinos:
        sucesor = vecindad(funcion_x,n)
        edo_nuevo = costo(sucesor)
        delta = edo_nuevo - edo_anterior
        if delta > 0:
            if random.random() >= math.exp((-delta)/(K*temp)):
                # TODO eliminar el sucesor
                sucesor = []
                edo_nuevo = 0
            else:
                edo_anterior = edo_nuevo
                funcion_x = sucesor
        else:
            edo_anterior = edo_nuevo
            funcion_x = sucesor
        vecinos_revisados = vecinos_revisados + 1
    temp = temp * alfa


print("\n")
print("Valores Finales: ", funcion_x)
print("costo igual a: ", edo_anterior)
print("\n")
