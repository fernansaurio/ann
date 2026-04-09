/*UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 5 - Asignacion 1

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

#include <stdio.h>
#include <math.h>

double f(double x) {
    return -0.4 * x * x + 2.3 * x + 2.2;
}

int main() {
    double xa = 6.0, xb = 7.0, xc, error = 100.0;
    double tol = 0.001; // 0.1%
    int iter = 1, max_iter = 100;

    printf("--- Metodo de la Secante (ANSI C) ---\n");
    printf("Iter |      xa      |      xb      |      xc      |   Error %%\n");
    
    while (error > tol && iter < max_iter) {
        double fa = f(xa);
        double fb = f(xb);
        
        xc = xa - fa * (xb - xa) / (fb - fa);
        error = fabs((xc - xa) / xc) * 100.0; // Error relativo
        
        printf(" %2d  | %12.6f | %12.6f | %12.6f | %10.4f\n", iter, xa, xb, xc, error);
        
        xa = xb;
        xb = xc;
        iter++;
    }
    printf("\nRaiz aproximada: %lf\n", xc);
    return 0;
}