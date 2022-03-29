import random


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

W = input('Ingresa el peso maximo que puede soportar la mochila: ')
W = int(W)


def fitness(mochila):
    Waux = W
    valmax = 0
    for j, objeto in enumerate(mochila):
        # Evaluando los objetos que estan dentro de la mochila
        objeto_actual = lista_objetos[j]
        if objeto == '1':
            Waux = Waux - objeto_actual.peso
            valmax = valmax + objeto_actual.valor

    if Waux < 0:
        valmax = 0

    return int(valmax)


def mutar_bit(bit, i, mochila):
    nbit = 0
    if bit == '0':
        nbit = 1
    new_mochila = mochila[0:i] + str(nbit) + mochila[i+1:]
    return new_mochila


def generar_random(num):
    nmochila = ""
    for i in range(num):
        nmochila = nmochila + str(random.randint(0, 1))
    return nmochila


N = input('Ingresa el número de evaluaciones: ')
N = int(N)
# La var mochila es una cadena binaria
mochila = generar_random(n)

fitness_actual = fitness(mochila)
eval = 1

print("Mochila Inicial: " + mochila +
      " con fitness igual a: " + str(fitness_actual) + "\n")

while eval < N:
    nuevas_fitness = []

    # heapq.heapify(nuevas_fitness)
    cadenas = []
    # i=el indice de la iteración bit=el valor en el indice de la cadena
    for i, bit in enumerate(mochila):
        mochila = mutar_bit(bit, i, mochila)
        cadenas.append(mochila)
        nuevas_fitness.append(fitness(mochila))
        eval += 1
    maxaux = max(nuevas_fitness)
    if maxaux > fitness_actual:
        indice = nuevas_fitness.index(maxaux)
        mochila = cadenas[indice]
        fitness_actual = maxaux
    else:
        mochila = generar_random(n)
        fitness_actual = fitness(mochila)
        eval += 1

print("Mochila Final: " + mochila +
      " con fitness igual a: " + str(fitness_actual) + "\n")
