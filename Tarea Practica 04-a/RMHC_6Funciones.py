import random
import copy
import math
from time import time


def fitness(funcion):
    valmax = 0
    for i in funcion:
        valmax += i**2
    return valmax

# Alpine 1 Function


def fitness1(funcion):
    valmax = 0
    for i in funcion:
        valmax += abs(i*(math.sin(i))+0.1*(i))
    return valmax

# Dixon & Price Function


def fitness2(funcion):
    valmax = (funcion[0] - 1)**2
    for i in range(1, len(funcion)):
        valmax += i*(2*math.sin(funcion[i])-funcion[i-1])**2
    return valmax

# Quintic Function


def fitness3(funcion):
    valmax = 0
    for i in funcion:
        valmax += abs((i**5)-(3*(i**4))+(4*(i**3))-(2*(i**2))-(10*i)-4)
    return valmax

# Schwefel 2.23 Function


def fitness4(funcion):
    valmax = 0
    for i in funcion:
        valmax += i**10
    return valmax

# Streched V Sine Wave Function


def fitness5(funcion):
    valmax = 0
    for i in range(len(funcion)-1):
        valmax += ((funcion[i+1]**2 + funcion[i]**2)**0.25) * \
            ((math.sin(50*((funcion[i+1]**2 + funcion[i]**2)**0.1))**2)+0.1)
    return valmax

# Sum Squares Function


def fitness6(funcion):
    valmax = 0
    for j, xi in enumerate(funcion):
        valmax += j * (xi**2)
    return valmax


def mutar_bit(locus, funcion):
    new_funcion = funcion.copy()
    new_funcion[locus] = random.uniform(-10, 10)
    return new_funcion


def rmhc():
    n = 30
    N = 500

    funcion_x = []
    for i in range(n):
        funcion_x.append(random.uniform(-10, 10))

    fitness_actual = fitness3(funcion_x)
    eval = 1

    while eval < N:
        locus = random.randint(0, n-1)
        nueva_funcion_x = mutar_bit(locus, funcion_x)
        nueva_fitness = fitness3(nueva_funcion_x)
        eval += 1

        if nueva_fitness <= fitness_actual:
            funcion_x = nueva_funcion_x
            fitness_actual = nueva_fitness

    print(fitness_actual)


for i in range(20):
    start_time = time()
    rmhc()
    #print("%s" % (time() - start_time))
