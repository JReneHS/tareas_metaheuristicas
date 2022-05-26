from copy import copy
import random
import math
from time import time
import statistics

tam_cromosoma = 30
tam_poblacion = 20
#generacion_global = 1
umbral = 0.1
prob_cruzamiento = 0.5

#poblacion = []
#nueva_poblacion = []


class Gen:
    cromosoma = []
    aptitud = float
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.calcular_aptitud3()
        self.generacion = generacion

# **********************************************************************************************************************

# Alpine 1 Function
    def calcular_aptitud1(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += abs(i*(math.sin(i))+0.1*(i))
        self.aptitud = valmax

# Dixon & Price Function
    def calcular_aptitud2(self):
        valmax = (self.cromosoma[0] - 1)**2
        for i in range(1, tam_cromosoma):
            valmax += i*(2*math.sin(self.cromosoma[i])-self.cromosoma[i-1])**2
        self.aptitud = valmax

# Quintic Function
    def calcular_aptitud3(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += abs((i**5)-(3*(i**4))+(4*(i**3))-(2*(i**2))-(10*i)-4)
        self.aptitud = valmax

# Schwefel 2.23 Function
    def calcular_aptitud4(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += i**10
        self.aptitud = valmax

# Streched V Sine Wave Function
    def calcular_aptitud5(self):
        valmax = 0
        for i in range(tam_cromosoma-1):
            valmax += ((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.25)*(
                (math.sin(50*((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.1))**2)+0.1)
        self.aptitud = valmax

# Sum Squares Function
    def calcular_aptitud6(self):
        valmax = 0
        for j, xi in enumerate(self.cromosoma):
            valmax += j * (xi**2)
        self.aptitud = valmax

# **********************************************************************************************************************

    def mutacion(self):
        for i in range(tam_cromosoma):
            if random.random() < umbral:
                self.cromosoma[i] = random.uniform(-10, 10)

    def __str__(self):
        cromosoma_str = [round(x, 2) for x in self.cromosoma]
        return "< Crom: " + str(cromosoma_str) + " Apt: " + str(self.aptitud) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [random.uniform(-10, 10) for _ in range(tam_cromosoma)]
    random.shuffle(cromosoma)
    return cromosoma


def seleccion_proporcional(poblacion):

    probabilidad = []
    probTotal = 0
    flecha = random.random()
    ruleta = [0]

    for i in poblacion:
        probTotal += i.aptitud

    for i in poblacion:
        probabilidad.append(i.aptitud / probTotal)

    for i in range(tam_poblacion):
        ruleta.append(probabilidad[i]+ruleta[i])

    ruleta.append(flecha)
    ruleta.sort()
    posicion = ruleta.index(flecha)
    apareamiento = poblacion[posicion-1]

    return apareamiento


def uniform_crossover(gen1, gen2):
    descendienteA = []
    descendienteB = []

    for j in range(tam_cromosoma):
        if random.random() < 0.5:
            descendienteA.append(gen1.cromosoma[j])
            descendienteB.append(gen2.cromosoma[j])
        else:
            descendienteA.append(gen2.cromosoma[j])
            descendienteB.append(gen1.cromosoma[j])
    return descendienteA, descendienteB


def replacement(poblacion, nueva_poblacion):
    poblacion.clear()
    poblacion.extend(nueva_poblacion)
    nueva_poblacion.clear()

# **********************************************************************************************************************


def GA():
    poblacion = []
    nueva_poblacion = []
    generacion_global = 1
    evaluaciones = 0

    # Generacion Inicial aleatoria
    for _ in range(tam_poblacion):
        poblacion.append(Gen(generacion_global, generar_cromosoma()))
        evaluaciones += 1

    # Iteracion para 500 generaciones
    while generacion_global < 500:
        # Generando nueva poblacion
        generacion_global += 1
        while len(nueva_poblacion) != tam_poblacion:

            if random.random() > prob_cruzamiento:
                continue

            gen1 = seleccion_proporcional(poblacion)
            gen2 = seleccion_proporcional(poblacion)
            # Cruzamiento de los padres
            crom_des1, crom_des2 = uniform_crossover(gen1, gen2)
            descendiente1 = Gen(generacion_global, crom_des1)
            descendiente2 = Gen(generacion_global, crom_des2)
            # Mutacion del descendiente
            descendiente1.mutacion()
            descendiente2.mutacion()

            descendiente1.calcular_aptitud3()
            descendiente2.calcular_aptitud3()
            evaluaciones += 2

            # Insertando el descendiente en la nueva poblacion
            nueva_poblacion.append(descendiente1)
            nueva_poblacion.append(descendiente2)

        replacement(poblacion, nueva_poblacion)

    return min(poblacion, key=lambda x: x.aptitud)


aptitudes = []
tiempo = []

for i in range(20):
    start_time = time()
    aptitudes.append(GA().aptitud)
    tiempo.append(time() - start_time)

mejorA = min(aptitudes)
peorA = max(aptitudes)
meanA = statistics.mean(aptitudes)
medianA = statistics.median(aptitudes)
sigmaA = statistics.pstdev(aptitudes)

mejorT = min(tiempo)
peorT = max(tiempo)
meanT = statistics.mean(tiempo)
medianT = statistics.median(tiempo)
sigmaT = statistics.pstdev(tiempo)

print("aptitud: ")
print(str(round(mejorA, 2)) + " " + str(round(peorA, 2)) + " " +
      str(round(meanA, 2)) + " " + str(round(medianA, 2)) + " " + str(round(sigmaA, 2)))
print("Tiempo: ")
print(str(round(mejorT, 2)) + " " + str(round(peorT, 2)) + " " +
      str(round(meanT, 2)) + " " + str(round(medianT, 2)) + " " + str(round(sigmaT, 2)))
