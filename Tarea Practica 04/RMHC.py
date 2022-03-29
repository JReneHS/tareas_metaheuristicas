import random


def fitness(funcion):
    valmax = int(0)
    for i in funcion:
        valmax += (i)**2
    return int(valmax)


def mutar_bit(locus, funcion):
    new_funcion = funcion
    new_funcion[locus] = random.randint(-10, 10)
    return new_funcion


n = input('Ingresa el número de elementos de la Sumatoria (D): ')
n = int(n)

N = input('Ingresa el número de evaluaciones: ')
N = int(N)
# La var mochila hace referencia a la var best evaluated
funcion_x = [0]*n
for i in range(n):
    funcion_x[i] = random.randint(-10, 10)

fitness_actual = fitness(funcion_x)
# La var n se usará como length
eval = 1
print("\n")
print("Valores Iniciales: ", funcion_x)
print("fitness igual a: ", fitness_actual)

while eval < N:
    locus = random.randint(0, n-1)
    nueva_funcion_x = mutar_bit(locus, funcion_x)
    nueva_fitness = fitness(nueva_funcion_x)
    eval += 1

    if nueva_fitness <= fitness_actual:
        funcion_x = nueva_funcion_x
        fitness_actual = nueva_fitness

    print("Valores: ", funcion_x)
    print("fitness: ", fitness_actual)


print("\n")
print("Valores Finales: ", funcion_x)
print("fitness igual a: ", fitness_actual)
print("\n")
