import random

k = 2
popsize = 10
poblacion = []
torneo = []
apareamiento = []

for i in range(popsize):
    poblacion.append(random.uniform(0,20))

print(poblacion)

for i in range(k):
    seleccion = random.randint(0,len(poblacion)-1)
    torneo.append(poblacion[seleccion])
    poblacion.pop(seleccion)

print(poblacion)
print(torneo)

apareamiento.append(max(torneo))

print(apareamiento)






    



