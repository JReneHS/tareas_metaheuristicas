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

W = input('Ingresa el peso máximo que puede soportar la mochila: ')
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


def mutar_bit(locus, mochila):
    bit = 0
    if mochila[locus] == '0':
        bit = 1
    new_mochila = mochila[0:locus] + str(bit) + mochila[locus+1:]
    return new_mochila


def generar_random(num):
    nmochila = ""
    for i in range(num):
        nmochila = nmochila + str(random.randint(0, 1))
    return nmochila


N = input('Ingresa el número de evaluaciones: ')
N = int(N)
# La var mochila hace referencia a la var best evaluated
mochila = generar_random(n)

fitness_actual = fitness(mochila)
# La var n se usará como length
eval = 1
print("Mochila Inicial: " + mochila +
      " con fitness igual a: " + str(fitness_actual) + "\n")

while eval < N:
    locus = random.randint(0, n-1)
    nueva_mochila = mutar_bit(locus, mochila)
    nueva_fitness = fitness(nueva_mochila)
    eval += 1

    if nueva_fitness >= fitness_actual:
        mochila = nueva_mochila
        fitness_actual = nueva_fitness


print("Mochila Final: " + mochila +
      " con fitness igual a: " + str(fitness_actual) + "\n")
