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
        self.calcular_aptitud()
        self.generacion = generacion

# **********************************************************************************************************************

    def calcular_aptitud(self):
        valmax = 0.0
        for i in self.cromosoma:
            valmax += i**2
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

            descendiente1.calcular_aptitud()
            descendiente2.calcular_aptitud()
            evaluaciones += 2
            # Remplazo Elitita
            elitism_replacement(poblacion, descendiente1)
            elitism_replacement(poblacion, descendiente2)

    aptitudes = []
    for i in poblacion:
        aptitudes.append(i.aptitud)

    mejor = min(aptitudes)
    peor = max(aptitudes)
    mean = statistics.mean(aptitudes)
    median = statistics.median(aptitudes)
    sigma = statistics.pstdev(aptitudes)

    return str(mejor) + " " + str(peor) + " " + str(mean) + " " + str(median) + " " + str(sigma)


for i in range(20):
    start_time = time()
    strr = GA()
    print(strr ,(time() - start_time))
