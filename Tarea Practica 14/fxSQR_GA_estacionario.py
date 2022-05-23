from copy import copy
import random

tam_cromosoma = 10
tam_poblacion = 20
generacion_global = 1
k_torneo = 2  # tam de la poblacion del torneo

humbral = 0.1

poblacion = []


class Gen:
    cromosoma = []
    aptitud = int
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.calcular_aptitud()
        self.generacion = generacion

    def calcular_aptitud(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += i**2
        self.aptitud = int(valmax)

    def mutacion(self):
        for i in range(tam_cromosoma):
            if random.random() < humbral:
                self.cromosoma[i] = random.uniform(-10, 10)

    def __str__(self):
        cromosoma_str = [round(x, 2) for x in self.cromosoma]
        return "< Crom: " + str(cromosoma_str) + " Apt: " + str(self.aptitud) + " Gen: " + str(self.generacion) + " >"


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

    for j in range(tam_cromosoma):
        if random.random() < 0.5:
            descendienteA.append(gen1.cromosoma[j])
        else:
            descendienteA.append(gen2.cromosoma[j])
    return descendienteA


def elitism_replacement(poblacion, descendiente):
    # Seleccion de Peor (Minimizar)
    reemplazo = max(poblacion, key=lambda x: x.aptitud)

    if descendiente.aptitud < reemplazo.aptitud:
        poblacion.pop(poblacion.index(reemplazo))
        poblacion.append(descendiente)

# **********************************************************************************************************************


# Generacion Inicial aleatoria
for _ in range(tam_poblacion):
    poblacion.append(Gen(generacion_global, generar_cromosoma()))

print(min(poblacion, key=lambda x: x.aptitud))

# Iteracion para 500 generaciones
while generacion_global < 500:
    # Generando nueva poblacion
    generacion_global += 1
    gen1 = seleccion_torneo(poblacion)
    gen2 = seleccion_torneo(poblacion)
    # Cruzamiento de los padres
    cromosoma_descendiente = uniform_crossover(gen1, gen2)
    descendiente = Gen(generacion_global, cromosoma_descendiente)
    # Mutacion del descendiente
    descendiente.mutacion()
    descendiente.calcular_aptitud()
    # Remplazo Elitita
    elitism_replacement(poblacion, descendiente)

    print(min(poblacion, key=lambda x: x.aptitud))
