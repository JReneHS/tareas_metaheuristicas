from copy import copy
import random

tam_cromosoma = 10
tam_poblacion = 20
generacion_global = 1
k_torneo = 2  # tam de la poblacion del torneo

poblacion = []
nueva_poblacion = []


class Gen:
    cromosoma = []
    aptitud = int
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.aptitud = self.calcular_aptitud()
        self.generacion = generacion

    def calcular_aptitud(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += i**2
        return valmax

    def mutacion(self):
        self.cromosoma[random.randint(
            0, tam_cromosoma-1)] = random.uniform(-10, 10)

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


def replacement(poblacion, nueva_poblacion):
    poblacion.clear()
    poblacion.extend(nueva_poblacion)
    nueva_poblacion.clear()

# **********************************************************************************************************************


# Generacion Inicial aleatoria
for _ in range(tam_poblacion):
    poblacion.append(Gen(generacion_global, generar_cromosoma()))

print(min(poblacion, key=lambda x: x.aptitud))

# Iteracion para 500 generaciones
while generacion_global < 500:
    # Generando nueva poblacion
    generacion_global += 1
    while len(nueva_poblacion) != tam_poblacion:
        gen1 = seleccion_torneo(poblacion)
        gen2 = seleccion_torneo(poblacion)
        # Cruzamiento de los padres
        cromosoma_descendiente = uniform_crossover(gen1, gen2)
        descendiente = Gen(generacion_global, cromosoma_descendiente)
        # Mutacion del descendiente
        descendiente.mutacion()
        # Insertando el descendiente en la nueva poblacion
        nueva_poblacion.append(descendiente)

    replacement(poblacion, nueva_poblacion)
    print(min(poblacion, key=lambda x: x.aptitud))
