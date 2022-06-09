import random


tam_cromosoma = 3
tam_poblacion = 10
k_torneo = 2  # tam de la poblacion del torneo
humbral = 0.8
prob_cruzamiento = 0.6
iteraciones = 50
tam_imagen = 5

#imagen = [[250, 201, 100], [25, 251, 10], [125, 150, 7]]
imagen = [[random.randint(0, 255) for _ in range(tam_imagen)]
          for _ in range(tam_imagen)]


class Gen:
    cromosoma = []
    aptitud = float
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.calcular_aptitud()
        self.generacion = generacion

# **********************************************************************************************************************

# Alpine 1 Function
    def calcular_aptitud(self):
        parametros = [[], [], []]
        for i in imagen:
            for j in i:
                dist_pixel = []
                dist_pixel.append(minkowsky(j, self.cromosoma[0]))
                dist_pixel.append(minkowsky(j, self.cromosoma[1]))
                dist_pixel.append(minkowsky(j, self.cromosoma[2]))

                segmentacion = dist_pixel.index(min(dist_pixel))

                if segmentacion == 0:
                    parametros[0].append(j)
                elif segmentacion == 1:
                    parametros[1].append(j)
                elif segmentacion == 2:
                    parametros[2].append(j)

        dist_min = [[], [], []]

        for i in range(3):
            aux = []
            if i == 0:
                aux.extend(parametros[1])
                aux.extend(parametros[2])
            elif i == 1:
                aux.extend(parametros[0])
                aux.extend(parametros[2])
            elif i == 2:
                aux.extend(parametros[0])
                aux.extend(parametros[1])
            for j in range(len(parametros[i])):
                aux2 = [minkowsky(parametros[i][j], x) for x in aux]
                dist_min[i].extend(aux2)

        dist_max = [[0], [0], [0]]

        for i in range(3):
            for j in range(len(parametros[i])):
                for k in range(j+1, len(parametros[i])):
                    dist_max[i].append(
                        minkowsky(parametros[i][j], parametros[i][k]))

        for i in dist_min:
            if len(i) == 0:
                i.append(0)

        self.aptitud = min([min(e) for e in dist_min]) / \
            max([max(u) for u in dist_max])


# **********************************************************************************************************************


    def mutacion(self):
        for i in range(tam_cromosoma):
            if random.random() < humbral:
                self.cromosoma[i] = random.randint(0, 255)

    def __str__(self):

        return "< Crom: " + str(self.cromosoma) + " Apt: " + str(round(self.aptitud, 3)) + " Gen: " + str(self.generacion) + " >"


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [random.randint(0, 255) for _ in range(tam_cromosoma)]

    return cromosoma


def minkowsky(x, y):
    return abs(x-y)


def seleccion_torneo(poblacion):
    torneo = []
    for i in range(k_torneo):
        seleccion = random.randint(0, tam_poblacion - 1)
        gen = poblacion[seleccion]
        torneo.append(gen)
    return max(torneo, key=lambda x: x.aptitud)


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


poblacion = []
nueva_poblacion = []
generacion_global = 1

# Generacion Inicial aleatoria
for _ in range(tam_poblacion):
    poblacion.append(Gen(generacion_global, generar_cromosoma()))

print(max(poblacion, key=lambda x: x.aptitud))

# Iteracion para 500 generaciones
while generacion_global < iteraciones:
    # Generando nueva poblacion
    generacion_global += 1
    while len(nueva_poblacion) != tam_poblacion:

        if random.random() > prob_cruzamiento:
            continue

        gen1 = seleccion_torneo(poblacion)
        gen2 = seleccion_torneo(poblacion)
        # Cruzamiento de los padres
        crom_des1, crom_des2 = one_point_crossover(gen1, gen2)
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
    print(max(poblacion, key=lambda x: x.aptitud))
