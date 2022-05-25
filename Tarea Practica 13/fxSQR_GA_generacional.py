from copy import copy
import random

tam_cromosoma = 10
tam_poblacion = 20
generacion_global = 1
k_torneo = 2  # tam de la poblacion del torneo
humbral = 0.1
prob_cruzamiento = 0.6

poblacion = []
nueva_poblacion = []


class Gen:
    cromosoma = []
    aptitud = float
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.calcular_aptitud()
        self.generacion = generacion

    def calcular_aptitud(self):
        valmax = 0
        for i in self.cromosoma:
            valmax += i**2
        self.aptitud = float(valmax)

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


# Generacion Inicial aleatoria
for _ in range(tam_poblacion):
    poblacion.append(Gen(generacion_global, generar_cromosoma()))

print(min(poblacion, key=lambda x: x.aptitud))

# Iteracion para 500 generaciones
while generacion_global < 5000:
    # Generando nueva poblacion
    generacion_global += 1
    while len(nueva_poblacion) != tam_poblacion:

        if random.random() > prob_cruzamiento:
            continue

        gen1 = seleccion_torneo(poblacion)
        gen2 = seleccion_torneo(poblacion)
        # Cruzamiento de los padres
        crom_des1, crom_des2 = uniform_crossover(gen1, gen2)
        descendiente1 = Gen(generacion_global, crom_des1)
        descendiente2 = Gen(generacion_global, crom_des2)
        # Mutacion del descendiente
        descendiente1.mutacion()
        descendiente2.mutacion()

        descendiente1.calcular_aptitud()
        descendiente2.calcular_aptitud()
        # Insertando el descendiente en la nueva poblacion
        nueva_poblacion.append(descendiente1)
        nueva_poblacion.append(descendiente2)

    replacement(poblacion, nueva_poblacion)
    print(min(poblacion, key=lambda x: x.aptitud))
