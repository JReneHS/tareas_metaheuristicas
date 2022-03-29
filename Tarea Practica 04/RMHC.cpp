#include <bits/stdc++.h>

using namespace std;

int fitness(vector<int> &funcion)
{
    int valmax = 0;
    for (auto &i : funcion)
    {
        valmax += i * i;
    }
    return valmax;
}

vector<int> mutar_bit(int locus, vector<int> &funcion)
{
    srand(time(NULL));
    vector<int> nueva_funcion;
    for (auto i : funcion)
    {
        nueva_funcion.push_back(i);
    }

    nueva_funcion[locus] = rand() % 11;
    if (rand() % 2 == 0)
    {
        nueva_funcion[locus] = -nueva_funcion[locus];
    }
    return nueva_funcion;
}

void imprimir_datos(string pos, int fitness, vector<int> &funcion)
{
    cout << "Valores " << pos << ": [";
    for (auto &i : funcion)
    {
        cout << i << "  ";
    }
    cout << "] Con Fitness: " << fitness << "\n\n";
}

int main(int argc, const char *argv[])
{
    srand(time(NULL));
    cout << "Ingrese el numero de Elementos (D): ";
    int D;
    cin >> D;
    cout << "Ingrese el numero de Evaluaciones (N): ";
    int N;
    cin >> N;

    vector<int> funcion_x(D, 0);
    for (int i = 0; i < D; i++)
    {
        funcion_x[i] = rand() % 11;
        if (rand() % 2 == 0)
        {
            funcion_x[i] = -funcion_x[i];
        }
    }
    int fitness_actual = fitness(funcion_x);
    int eval = 1;
    cout << "\n\n";
    imprimir_datos("Iniciales", fitness_actual, funcion_x);

    while (eval < N)
    {
        int locus = rand() % D;
        vector<int> nueva_funcion = mutar_bit(locus, funcion_x);
        int nueva_fitness = fitness(nueva_funcion);

        if (nueva_fitness <= fitness_actual)
        {
            funcion_x = nueva_funcion;
            fitness_actual = nueva_fitness;
        }
        eval++;
    }

    imprimir_datos("Finales", fitness_actual, funcion_x);

    return 0;
}
