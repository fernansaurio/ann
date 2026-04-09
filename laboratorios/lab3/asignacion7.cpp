/*
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 7

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

#include <iostream>
#include <cmath>

// Definición del puntero a función
typedef double (*FuncPtr)(double);

// Función a evaluar
double funcion_problema(double x) {
    return -0.5 * x * x + 2.5 * x + 4.5;
}

// Algoritmo de falsa posición
double falsa_posicion(FuncPtr f, double a, double b, double tol, int max_iter, int* iteraciones) {
    *iteraciones = 0;
    if (f(a) * f(b) >= 0) {
        std::cerr << "El intervalo no contiene una raiz." << std::endl;
        return NAN;
    }
    double c = a;
    for (int i = 0; i < max_iter; ++i) {
        // Fórmula de la falsa posición
        c = (a * f(b) - b * f(a)) / (f(b) - f(a));
        
        if (std::abs(f(c)) < tol) return c;
        
        if (f(c) * f(a) < 0) {
            b = c;
        } else {
            a = c;
        }
        (*iteraciones)++;
    }
    return c;
}

int main() {
    int iters;
    double tolerancia = 0.0001;
    
    // Llamada a la función con el intervalo [5, 10]
    double raiz = falsa_posicion(funcion_problema, 5.0, 10.0, tolerancia, 100, &iters);
    
    std::cout << "--- Metodo de Falsa Posicion (C++) ---" << std::endl;
    std::cout << "Raiz aproximada: " << raiz << std::endl;
    std::cout << "Iteraciones realizadas: " << iters << std::endl;
    
    return 0;
}