from copy import copy
import random

tam_cromosoma = 10
tam_poblacion = 20
generacion_global = 1
k_torneo = 2  # tam de la poblacion del torneo

valor_objetos = [25, 21, 13, 19, 24, 22, 12, 21, 15, 13]
peso_objetos = [20, 16, 27, 16, 15, 30, 35, 15, 40, 48]
peso_maximo = 100

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
        peso_aux = peso_maximo
        valmax = 0
        for j in range(tam_cromosoma):
            # Evaluando los objetos que estan dentro de la mochila
            if self.cromosoma[j] == 1:
                peso_aux = peso_aux - peso_objetos[j]
                valmax = valmax + valor_objetos[j]

        if peso_aux < 0:
            valmax = -1

        self.aptitud = int(valmax)

    def mutacion(self):
        for i in range(tam_cromosoma):
            if random.random() < humbral:
                self.cromosoma[i] = random.randint(0, 1)

    def __str__(self):
        return "< Crom: " + str(self.cromosoma) + " Apt: " + str(self.aptitud) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [random.randint(0, 1) for _ in range(tam_cromosoma)]
    random.shuffle(cromosoma)
    return cromosoma


def seleccion_torneo(poblacion):
    torneo = []
    for i in range(k_torneo):
        seleccion = random.randint(0, tam_poblacion - 1)
        gen = poblacion[seleccion]
        torneo.append(gen)
    return max(torneo, key=lambda x: x.aptitud)


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


def hamming_distance(gen1, gen2):
    result = 0
    if len(gen1.cromosoma) != len(gen2.cromosoma):
        print("Error: Los cromosomas no tienen el mismo tamaño")
    else:
        for x in range(tam_cromosoma):
            if gen1.cromosoma[x] != gen2.cromosoma[x]:
                result += 1
    return result


def crowding_replacement(poblacion, descendiente1, descendiente2, padre1, padre2):

    dis_11 = hamming_distance(padre1, descendiente1)
    dis_12 = hamming_distance(padre1, descendiente2)

    dis_21 = hamming_distance(padre2, descendiente1)
    dis_22 = hamming_distance(padre2, descendiente2)

    if (dis_11 + dis_22) <= (dis_12 + dis_21):
        gan1 = max(padre1, descendiente1, key=lambda x: x.aptitud)
        poblacion.append(gan1)
        gan2 = max(padre2, descendiente2, key=lambda x: x.aptitud)
        poblacion.append(gan2)
    else:
        gan1 = max(padre1, descendiente2, key=lambda x: x.aptitud)
        poblacion.append(gan1)
        gan2 = max(padre2, descendiente1, key=lambda x: x.aptitud)
        poblacion.append(gan2)

# **********************************************************************************************************************


# Generacion Inicial aleatoria
for _ in range(tam_poblacion):
    poblacion.append(Gen(generacion_global, generar_cromosoma()))

print(max(poblacion, key=lambda x: x.aptitud))

# Iteracion para 500 generaciones
while generacion_global < 500:
    # Generando nueva poblacion
    generacion_global += 1
    gen1 = seleccion_torneo(poblacion)
    gen2 = seleccion_torneo(poblacion)
    # Cruzamiento de los padres
    crom_des1, crom_des2 = uniform_crossover(gen1, gen2)
    des1 = Gen(generacion_global, crom_des1)
    des2 = Gen(generacion_global, crom_des2)
    # Mutacion del descendiente
    des1.mutacion()
    des2.mutacion()
    des1.calcular_aptitud()
    des2.calcular_aptitud()

    crowding_replacement(poblacion, des1, des2, gen1, gen2)
    print(max(poblacion, key=lambda x: x.aptitud))
