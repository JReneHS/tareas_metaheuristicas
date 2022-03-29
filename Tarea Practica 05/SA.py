import random
import math


class Objetos:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso


n = input('Ingresa el número de objetos que desea meter en la mochila: ')
n = int(n)

lista_objetos = []
for i in range(n):
    valor = input(f"Ingrese el valor del objeto {i}:  ")
    valor = int(valor)
    peso = input(f"Ingrese el peso del objeto {i}:  ")
    peso = int(peso)
    lista_objetos.append(Objetos(valor, peso))

W = input('Ingresa el peso máximo que puede soportar la mochila: ')
W = int(W)


def costo(mochila):
    Waux = W
    valmax = 0
    for j, objeto in enumerate(mochila):
        # Evaluando los objetos que estan dentro de la mochila
        objeto_actual = lista_objetos[j]
        if objeto == '1':
            Waux = Waux - objeto_actual.peso
            valmax = valmax + objeto_actual.valor

    if Waux < 0:
        valmax = -1

    return int(valmax)


def vecindad(mochila):
    bit = 0
    locus = random.randint(0, n - 1)
    if mochila[locus] == '0':
        bit = 1
    new_mochila = mochila[0:locus] + str(bit) + mochila[locus+1:]
    return new_mochila


def generar_random(num):
    nmochila = ""
    for i in range(num):
        nmochila = nmochila + str(random.randint(0, 1))
    return nmochila


def rechazar():
    return ""


temp_min = 0.1
temp_max = 300.0
vecinos = n - 1
alfa = 0.8
K = 1.0

mochila = generar_random(n)

edo_anterior = costo(mochila)

print("Mochila Inicial: " + mochila +
      " con Costo igual a: " + str(edo_anterior) + "\n")

temp = temp_max

while temp >= temp_min:
    vecinos_revisados = 0
    while vecinos_revisados < vecinos:
        sucesor = vecindad(mochila)
        edo_nuevo = costo(sucesor)
        delta = edo_nuevo - edo_anterior
        if delta < 0:
            if random.random() >= math.exp(delta/(K*temp)):
                sucesor = rechazar()
                edo_nuevo = 0
            else:
                edo_anterior = edo_nuevo
                mochila = sucesor
        else:
            edo_anterior = edo_nuevo
            mochila = sucesor
        vecinos_revisados = vecinos_revisados + 1
    temp = temp * alfa

print("Mochila Final: " + mochila +
      " con Costo igual a: " + str(edo_anterior) + "\n")
