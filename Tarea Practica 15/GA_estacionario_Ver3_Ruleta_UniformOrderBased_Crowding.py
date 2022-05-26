import math
import random
from time import time
import statistics


tam_cromosoma = 10
tam_poblacion = 10

umbral = 0.1

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
                ((math.sin(
                    50*((self.cromosoma[i+1]**2 + self.cromosoma[i]**2)**0.1))**2)+0.1)
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
            if random.random() < umbral:
                self.cromosoma[i] = random.uniform(-10, 10)

    def __str__(self):
        cromosoma_str = [round(x, 2) for x in self.cromosoma]
        return "< Crom: " + str(cromosoma_str) + " Apt: " + str(round(self.aptitud, 2)) + " Gen: " + str(self.generacion) + " >"


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
    evaluaciones = 0

    # Generacion Inicial aleatoria
    for _ in range(tam_poblacion):
        poblacion.append(Gen(generacion_global, generar_cromosoma()))
        evaluaciones += 1

    # Iteracion para 500 generaciones
    while evaluaciones < 500:
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

            descendiente1.fitness1()
            descendiente2.fitness1()
            evaluaciones += 2
            # Remplazo Elitita
            crowding_replacement(poblacion, descendiente1,
                                 descendiente2, gen1, gen2)
        else:
            poblacion.append(gen1)
            poblacion.append(gen2)

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
print(str(round(mejorA, 2)) + " " + str(round(peorA, 2)) + " " +
      str(round(meanA, 2)) + " " + str(round(medianA, 2)) + " " + str(round(sigmaA, 2)))
print("Tiempo: ")
print(str(round(mejorT, 2)) + " " + str(round(peorT, 2)) + " " +
      str(round(meanT, 2)) + " " + str(round(medianT, 2)) + " " + str(round(sigmaT, 2)))
