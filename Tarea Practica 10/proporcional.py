import random
import math

popsize = 10
poblacion = []
apareamiento = []
probabilidad = []
probTotal = 0
flecha = random.random()
ruleta=[0]

for i in range(popsize):
    poblacion.append(random.uniform(0,20))
    probTotal += poblacion[i] 

poblacion.sort()
print(poblacion)

for i in range(popsize): 
    probabilidad.append(poblacion[i]/probTotal)

print(probabilidad)
    
for i in range(popsize):     
    ruleta.append(probabilidad[i]+ruleta[i])

print(ruleta)

ruleta.append(flecha)
ruleta.sort()

posicion = ruleta.index(flecha)

apareamiento.append(poblacion[posicion-1])

print(apareamiento)