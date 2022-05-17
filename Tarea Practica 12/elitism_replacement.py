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


# Con Valores de Representaciones de Orden
def generar_cromosoma():
    cromosoma = [i+1 for i in range(tam_cromosoma)]
    random.shuffle(cromosoma)
    return cromosoma


def hamming(gen1, gen2):
    result = 0
    if len(gen1.cromosoma) != len(gen2.cromosoma):
        print("Error: Los cromosomas no tienen el mismo tamaño")
    else:
        for x in range(tam_cromosoma):
            if gen1.cromosoma[x] != gen2.cromosoma[x]:
                result += 1
    return result


poblacion = []

for _ in range(tam_poblacion):
    poblacion.append(Gen(1, generar_cromosoma()))

print("\n\nPoblacion inicial:")
for i in poblacion:
    print(i)

elite = max(poblacion, key=lambda x: x.aptitud)

reemplazo = random.randint(0, tam_poblacion-1)
bandera = True

if poblacion[reemplazo] != elite:
    bandera = False
    poblacion.pop(reemplazo)
    poblacion.append(Gen(2, generar_cromosoma()))

print("\n\n elite generacional:")
print(elite)
print("Distancia Hamming:")
print(hamming(elite, poblacion[reemplazo]))

print("\n\nPoblacion Final:")
for i in poblacion:
    print(i)

if bandera:
    print("\n<< Se intento reemplazar al elite >>")
