import math
import random
from time import time
import statistics


tam_cromosoma = 10
tam_poblacion = 50
k_torneo = 2  # tam de la poblacion del torneo

humbral = 0.1

prob_cruzamiento = 0.5


class Gen:
    cromosoma = []
    aptitud = float
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.fitness1()
        self.generacion = generacion

# **********************************************************************************************************************
    # Alpine 1 Function

    def fitness1(self):
        valmax = 0.0
        for i in self.cromosoma:
            valmax += abs(i*(math.sin(i))+0.1*(i))
        self.aptitud = valmax


    # Dixon & Price Function


    def fitness2(self):
        valmax = (self.cromosoma[0] - 1)**2
        for i in range(1, tam_cromosoma):
            valmax += i*(2*math.sin(self.cromosoma[i])-self.cromosoma[i-1])**2
        self.aptitud = valmax

    # Quintic Function


    def fitness3(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += abs((i**5)-(3*(i**4))+(4*(i**3))-(2*(i**2))-(10*i)-4)
        self.aptitud = valmax

    # Schwefel 2.23 Function


    def fitness4(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += i**10
        self.aptitud = valmax

    # Streched V Sine Wave Function


    def fitness5(self):
        valmax = 0
        for i in range(tam_cromosoma - 1):
            valmax += ((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.25) * \
                ((math.sin(50*((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.1))**2)+0.1)
        self.aptitud = valmax

    # Sum Squares Function


    def fitness6(self):
        valmax = 0
        for j, xi in enumerate(self.cromosoma):
            valmax += j * (xi**2)
        self.aptitud = valmax

# **********************************************************************************************************************

    def mutacion(self):
        for i in range(tam_cromosoma):
            if random.random() < humbral:
                self.cromosoma[i] = random.uniform(-10, 10)

    def __str__(self):
        cromosoma_str = [round(x, 2) for x in self.cromosoma]
        return "< Apt: " + str(round(self.aptitud,2)) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [random.uniform(-10, 10) for _ in range(tam_cromosoma)]
    random.shuffle(cromosoma)
    return cromosoma


def seleccion_torneo(poblacion):
    torneo = []
    for i in range(k_torneo):
        seleccion = random.randint(0, tam_poblacion - 1)
        gen = poblacion[seleccion]
        torneo.append(gen)
    return min(torneo, key=lambda x: x.aptitud)


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


def elitism_replacement(poblacion, descendiente):
    # Seleccion de Peor (Minimizar)
    reemplazo = max(poblacion, key=lambda x: x.aptitud)

    if descendiente.aptitud < reemplazo.aptitud:
        poblacion.pop(poblacion.index(reemplazo))
        poblacion.append(descendiente)

# **********************************************************************************************************************

def GA():
    poblacion = []
    generacion_global = 1
    evaluaciones = 0

    # Generacion Inicial aleatoria
    for _ in range(tam_poblacion):
        poblacion.append(Gen(generacion_global, generar_cromosoma()))
        evaluaciones += 1

    # Iteracion para 500 evaluaciones
    while evaluaciones < 500:
        # Generando nueva poblacion
        generacion_global += 1
        gen1 = seleccion_torneo(poblacion)
        gen2 = seleccion_torneo(poblacion)
        # Probabilidad de Cruzamiento.
        if random.random() > prob_cruzamiento:
            # Cruzamiento de los padres
            crom_des1, crom_des2 = uniform_crossover(gen1, gen2)
            descendiente1 = Gen(generacion_global, crom_des1)
            descendiente2 = Gen(generacion_global, crom_des2)
            # Mutacion del descendiente
            descendiente1.mutacion()
            descendiente2.mutacion()

            descendiente1.fitness1()
            descendiente2.fitness1()
            evaluaciones += 2
            # Remplazo Elitita
            elitism_replacement(poblacion, descendiente1)
            elitism_replacement(poblacion, descendiente2)

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
print(str(mejorA) + " " + str(peorA) + " " + str(meanA) + " " + str(medianA) + " " + str(sigmaA))
print("Tiempo: ")
print(str(mejorT) + " " + str(peorT) + " " + str(meanT) + " " + str(medianT) + " " + str(sigmaT))