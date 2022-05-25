import random


tam_cromosoma = 10
tam_poblacion = 10
generacion_global = 1

humbral = 0.1

prob_cruzamiento = 0.5

poblacion = []


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


def one_point_crossover(gen1, gen2):
    descendienteA = []
    descendienteB = []

    punto_corte = random.randint(1, tam_cromosoma-1)

    descendienteA = gen1.cromosoma[:punto_corte] + gen2.cromosoma[punto_corte:]
    descendienteB = gen2.cromosoma[:punto_corte] + gen1.cromosoma[punto_corte:]

    return descendienteA, descendienteB


def random_replacement(poblacion, descendiente):
    reemplazo = random.randint(0, tam_poblacion-1)
    poblacion.pop(reemplazo)
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
    gen1 = seleccion_proporcional(poblacion)
    gen2 = seleccion_proporcional(poblacion)
    # Probabilidad de Cruzamiento.
    if random.random() > prob_cruzamiento:
        # Cruzamiento de los padres
        crom_des1, crom_des2 = one_point_crossover(gen1, gen2)
        descendiente1 = Gen(generacion_global, crom_des1)
        descendiente2 = Gen(generacion_global, crom_des2)
        # Mutacion del descendiente
        descendiente1.mutacion()
        descendiente2.mutacion()

        descendiente1.calcular_aptitud()
        descendiente2.calcular_aptitud()
        # Remplazo Elitita
        random_replacement(poblacion, descendiente1)
        random_replacement(poblacion, descendiente2)

    print(min(poblacion, key=lambda x: x.aptitud))
    print(tam_poblacion == len(poblacion))
