from copy import copy
import random
import math
from time import time
import statistics

tam_cromosoma = 30
tam_poblacion = 20
#generacion_global = 1
# k_torneo = 2  # tam de la poblacion del torneo
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
        self.calcular_aptitud6()
        self.generacion = generacion

# **********************************************************************************************************************

# Alpine 1 Function
    def calcular_aptitud1(self):
        valmax = 0.0
        for i in self.cromosoma:
            valmax += abs(i*(math.sin(i))+0.1*(i))
        self.aptitud = valmax

# Dixon & Price Function
    def calcular_aptitud2(self):
        valmax = (self.cromosoma[0] - 1)**2
        for i in range(1, len(self.cromosoma)):
            valmax += i*(2*math.sin(self.cromosoma[i])-self.cromosoma[i-1])**2
        self.aptitud = valmax

# Quintic Function
    def calcular_aptitud3(self):
        valmax = 0.0
        for i in self.cromosoma:
            valmax += abs((i**5)-(3*(i**4))+(4*(i**3))-(2*(i**2))-(10*i)-4)
        self.aptitud = valmax

# Schwefel 2.23 Function
    def calcular_aptitud4(self):
        valmax = 0.0
        for i in self.cromosoma:
            valmax += i**10
        self.aptitud = valmax

# Streched V Sine Wave Function
    def calcular_aptitud5(self):
        valmax = 0.0
        for i in range(len(self.cromosoma)-1):
            valmax += ((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.25)*(
                (math.sin(50*((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.1))**2)+0.1)
        self.aptitud = valmax

# Sum Squares Function
    def calcular_aptitud6(self):
        valmax = 0.0
        for j, i in enumerate(self.cromosoma):
            valmax += j * (i**2)
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


def seleccion_ruleta(poblacion):

    flecha_ruleta = random.randint(0, len(poblacion) - 1)
    seleccion = poblacion.pop(flecha_ruleta)
    return seleccion


def one_point_crossover(gen1, gen2):
    descendienteA = []
    descendienteB = []

    punto_corte = random.randint(1, tam_cromosoma-1)

    descendienteA = gen1.cromosoma[:punto_corte] + gen2.cromosoma[punto_corte:]
    descendienteB = gen2.cromosoma[:punto_corte] + gen1.cromosoma[punto_corte:]

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

            gen1 = seleccion_ruleta(poblacion)
            gen2 = seleccion_ruleta(poblacion)
            # Cruzamiento de los padres
            crom_des1, crom_des2 = one_point_crossover(gen1, gen2)
            descendiente1 = Gen(generacion_global, crom_des1)
            descendiente2 = Gen(generacion_global, crom_des2)
            # Mutacion del descendiente
            descendiente1.mutacion()
            descendiente2.mutacion()

            descendiente1.calcular_aptitud6()
            descendiente2.calcular_aptitud6()
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
