import random
import math

tam_cromosoma = 10
tam_poblacion = 10


class Gen:
    cromosoma = []
    aptitud = int
    generacion = int

    def __init__(self, generacion, cromosoma):
        self.cromosoma = cromosoma
        self.aptitud = self.calcular_aptitud()
        self.generacion = generacion

    def calcular_aptitud(self):
        return sum(self.cromosoma) * random.randint(2, 5)

    def __str__(self):
        cromosoma_str = [round(x, 2) for x in self.cromosoma]
        return "< Crom: " + str(cromosoma_str) + " Apt: " + str(round(self.aptitud, 2)) + " Gen: " + str(self.generacion) + " >"


# Con valores Reales
def generar_cromosoma():
    cromosoma = [random.uniform(-10.0, 10.0) for _ in range(tam_cromosoma)]
    return cromosoma


def distancia_cromosoma(gen1, gen2):
    distancia = 0
    for i in range(tam_cromosoma):
        distancia += (gen1.cromosoma[i] - gen2.cromosoma[i])**2
    return math.sqrt(distancia)


def hamming(gen1, gen2):
    result = 0
    if len(gen1.cromosoma) != len(gen2.cromosoma):
        print("Error: Los cromosomas no tienen el mismo tamaño")
    else:
        for x in range(tam_cromosoma):
            if gen1.cromosoma[x] != gen2.cromosoma[x]:
                result += 1
    return result


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


poblacion = []

for _ in range(tam_poblacion):
    poblacion.append(Gen(1, generar_cromosoma()))

print("\n\nPoblacion Inicial:")
for i in poblacion:
    print(i)

pos1 = random.randint(0, tam_poblacion-1)
padre1 = poblacion.pop(pos1)
pos2 = random.randint(0, tam_poblacion-2)
padre2 = poblacion.pop(pos2)


des_crom1, des_crom2 = uniform_crossover(padre1, padre2)
descendiete1 = Gen(2, des_crom1)
descendiete2 = Gen(2, des_crom2)


dis_11 = distancia_cromosoma(padre1, descendiete1)
dis_12 = distancia_cromosoma(padre1, descendiete2)

dis_21 = distancia_cromosoma(padre2, descendiete1)
dis_22 = distancia_cromosoma(padre2, descendiete2)

if (dis_11 + dis_22) <= (dis_12 + dis_21):
    gan1 = max(padre1, descendiete1, key=lambda x: x.aptitud)
    poblacion.append(gan1)
    gan2 = max(padre2, descendiete2, key=lambda x: x.aptitud)
    poblacion.append(gan2)
else:
    gan1 = max(padre1, descendiete2, key=lambda x: x.aptitud)
    poblacion.append(gan1)
    gan2 = max(padre2, descendiete1, key=lambda x: x.aptitud)
    poblacion.append(gan2)


print("\n\nPoblacion Final:")
for i in poblacion:
    print(i)
