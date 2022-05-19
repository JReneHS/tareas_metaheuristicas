import random
import numpy as np

tam_cromosoma = 10
tam_poblacion = 30
generacion_global = 1
k_torneo = 2  # tam de la poblacion del torneo

ciudades = np.zeros((tam_poblacion+1, tam_poblacion+1), int)
for i in range(tam_poblacion+1):
    for j in range(tam_poblacion+1):
        if i == j:
            continue
        ciudades[i, j] = random.randint(1, 100)

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
        costo = 0
        origen = np.where(self.cromosoma == 1)
        inicio = origen
        j = 2
        n = tam_cromosoma
        while j < n:
            destino = np.where(self.cromosoma == j)
            costo += ciudades[origen[0], destino[0]]
            origen = destino
            j += 1
        costo += ciudades[origen[0], inicio[0]]
        return costo[0]

    def mutacion(self):
        indice1 = random.randint(0, tam_cromosoma-1)
        indice2 = random.randint(0, tam_cromosoma-1)
        aux = self.cromosoma[indice2]
        self.cromosoma[indice2] = self.cromosoma[indice1]
        self.cromosoma[indice1] = aux

    def __str__(self):
        return "< Crom: " + str(self.cromosoma) + " Apt: " + str(self.aptitud) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = np.zeros((tam_cromosoma), int)
    for i in range(tam_cromosoma):
        cromosoma[i] = i+1
    np.random.shuffle(cromosoma)
    return cromosoma


def seleccion_torneo(poblacion):
    torneo = []
    for i in range(k_torneo):
        seleccion = random.randint(0, tam_poblacion - 1)
        gen = poblacion[seleccion]
        torneo.append(gen)
    return min(torneo, key=lambda x: x.aptitud)


def uniform_order_based_crossover(cromosomaA, cromosomaB):
    # Inicializacion Plantilla binaria aleatoria
    template_binario = np.zeros((tam_cromosoma), int)

    # Rellenamos Plantilla binaria aleatoria
    for i in range(tam_cromosoma):
        if random.random() < 0.5:
            template_binario[i] = 1

    # Inicializacion de cromosomas Hijos
    descendienteA = np.zeros((tam_cromosoma), int)
    descendienteB = np.zeros((tam_cromosoma), int)

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
        crom_des1, crom_des2 = uniform_order_based_crossover(
            gen1.cromosoma, gen2.cromosoma)
        descendiente1 = Gen(generacion_global, crom_des1)
        descendiente2 = Gen(generacion_global, crom_des2)
        # Mutacion del descendiente
        descendiente1.mutacion()
        descendiente2.mutacion()
        # Insertando el descendiente en la nueva poblacion
        nueva_poblacion.append(descendiente1)
        nueva_poblacion.append(descendiente2)

    replacement(poblacion, nueva_poblacion)
    print(min(poblacion, key=lambda x: x.aptitud))
