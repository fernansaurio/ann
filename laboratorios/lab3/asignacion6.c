/*
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 3 - Asignacion 6

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

#include <stdio.h>
#include <math.h>

// Función a evaluar
double f(double x) {
    return -0.5 * x * x + 2.5 * x + 4.5;
}

int main() {
    double a = 5.0;
    double b = 10.0;
    double c;
    int iteraciones = 3;
    
    printf("Metodo de Biseccion en ANSI C\n");
    printf("Iter | c_aprox\n");
    printf("--------------\n");
    
    for (int i = 0; i < iteraciones; i++) {
        c = (a + b) / 2.0;
        printf("  %d  | %.4f\n", i + 1, c);
        
        // Determinar el nuevo intervalo
        if (f(a) * f(c) < 0) {
            b = c;
        } else {
            a = c;
        }
    }
    
    return 0;
}