import math
import random
from time import time
import statistics


tam_cromosoma = 10
tam_poblacion = 10

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
        return "< Crom: " + str(cromosoma_str) + " Apt: " + str(round(self.aptitud,2)) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [random.uniform(-10, 10) for _ in range(tam_cromosoma)]
    random.shuffle(cromosoma)
    return cromosoma


def seleccion_ruleta(poblacion):

    flecha_ruleta = random.randint(0, len(poblacion) - 1)
    seleccion = poblacion.pop(flecha_ruleta)
    return seleccion


def uniform_order_based_crossover(cromosomaA, cromosomaB):
    # Inicializacion Plantilla binaria aleatoria
    template_binario = [0 for _ in range(tam_cromosoma)]

    # Rellenamos Plantilla binaria aleatoria
    for i in range(tam_cromosoma):
        if random.random() < 0.5:
            template_binario[i] = 1

    # Inicializacion de cromosomas Hijos
    descendienteA = [0 for _ in range(tam_cromosoma)]
    descendienteB = [0 for _ in range(tam_cromosoma)]

    # Rellenamos Hijos con Plantilla binaria aleatoria
    for i in range(tam_cromosoma):
        if template_binario[i] == 1:
            descendienteA[i] = cromosomaA[i]
            descendienteB[i] = cromosomaB[i]

    buffer_hijo_A = []
    buffer_hijo_B = []

    # creando Buffer de genes restantes del Hijo A
    for i in range(tam_cromosoma):
        if not (cromosomaB[i] in descendienteA):
            buffer_hijo_A.append(cromosomaB[i])

    # creando Buffer de genes restantes del Hijo B
    for i in range(tam_cromosoma):
        if not (cromosomaA[i] in descendienteB):
            buffer_hijo_B.append(cromosomaA[i])

    # Rellenar los espacios restantes del Hijo A con los valores en orden del Padre B
    for i in range(tam_cromosoma):
        if template_binario[i] == 0:
            descendienteA[i] = buffer_hijo_A.pop(0)
            descendienteB[i] = buffer_hijo_B.pop(0)

    return descendienteA, descendienteB


def euclidean_distance(gen1, gen2):
    distancia = 0
    for i in range(tam_cromosoma):
        distancia += (gen1.cromosoma[i] - gen2.cromosoma[i])**2
    return math.sqrt(distancia)


def crowding_replacement(poblacion, descendiente1, descendiente2, padre1, padre2):

    dis_11 = euclidean_distance(padre1, descendiente1)
    dis_12 = euclidean_distance(padre1, descendiente2)

    dis_21 = euclidean_distance(padre2, descendiente1)
    dis_22 = euclidean_distance(padre2, descendiente2)

    if (dis_11 + dis_22) <= (dis_12 + dis_21):
        gan1 = min(padre1, descendiente1, key=lambda x: x.aptitud)
        poblacion.append(gan1)
        gan2 = min(padre2, descendiente2, key=lambda x: x.aptitud)
        poblacion.append(gan2)
    else:
        gan1 = min(padre1, descendiente2, key=lambda x: x.aptitud)
        poblacion.append(gan1)
        gan2 = min(padre2, descendiente1, key=lambda x: x.aptitud)
        poblacion.append(gan2)

# **********************************************************************************************************************

def GA():
    poblacion = []
    generacion_global = 1

    # Generacion Inicial aleatoria
    for _ in range(tam_poblacion):
        poblacion.append(Gen(generacion_global, generar_cromosoma()))

    # Iteracion para 500 generaciones
    while generacion_global < 500:
        # Generando nueva poblacion
        generacion_global += 1
        gen1 = seleccion_ruleta(poblacion)
        gen2 = seleccion_ruleta(poblacion)
        # Probabilidad de Cruzamiento.
        if random.random() > prob_cruzamiento:
            # Cruzamiento de los padres
            crom_des1, crom_des2 = uniform_order_based_crossover(
                gen1.cromosoma, gen2.cromosoma)
            descendiente1 = Gen(generacion_global, crom_des1)
            descendiente2 = Gen(generacion_global, crom_des2)
            # Mutacion del descendiente
            descendiente1.mutacion()
            descendiente2.mutacion()

            descendiente1.calcular_aptitud()
            descendiente2.calcular_aptitud()
            # Remplazo Elitita
            crowding_replacement(poblacion, descendiente1,
                                descendiente2, gen1, gen2)
        else:
            poblacion.append(gen1)
            poblacion.append(gen2)

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
