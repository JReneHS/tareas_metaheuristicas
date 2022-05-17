import random

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
        return sum(self.cromosoma) * random.randint(2, 10)

    def __str__(self):
        return "< Crom: " + str(self.cromosoma) + " Apt: " + str(self.aptitud) + " Gen:" + str(self.generacion) + " >"


# Con Valores Binarios
def generar_cromosoma():
    cromosoma = [random.randint(0, 1) for _ in range(tam_cromosoma)]
    return cromosoma


poblacion = []

for _ in range(tam_poblacion):
    poblacion.append(Gen(1, generar_cromosoma()))

print("\n\nPoblacion inicial:")
for i in poblacion:
    print(i)

reemplazo = random.randint(0, tam_poblacion-1)

poblacion.pop(reemplazo)

poblacion.append(Gen(2, [5 for _ in range(tam_cromosoma)]))

print("\n\nPoblacion Final:")
for i in poblacion:
    print(i)
