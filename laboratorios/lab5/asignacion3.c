/*UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 5 - Asignacion 3

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
    return x*x*x - 13*x - 12;
}

void muller(double x0, double x1, double x2, double tol, int max_iter) {
    double h1, h2, d1, d2, a, b, c, disc, x3, error = 100.0;
    
    printf("--- Metodo de Muller (ANSI C) ---\n");
    for(int i=0; i<max_iter; i++) {
        h1 = x1 - x0;
        h2 = x2 - x1;
        d1 = (f(x1) - f(x0)) / h1;
        d2 = (f(x2) - f(x1)) / h2;
        
        a = (d2 - d1) / (h2 + h1);
        b = a * h2 + d2;
        c = f(x2);
        
        disc = b*b - 4*a*c;
        if(disc < 0) {
            printf("Raices complejas detectadas.\n");
            return;
        }
        
        double s_disc = sqrt(disc);
        double den = (b < 0) ? b - s_disc : b + s_disc;
        
        x3 = x2 - (2*c) / den;
        error = fabs((x3 - x2) / x3) * 100.0;
        
        printf("Iter %d: Raiz = %lf, Error = %lf%%\n", i+1, x3, error);
        
        if(error < tol) break;
        
        x0 = x1;
        x1 = x2;
        x2 = x3;
    }
}

int main() {
    muller(4.5, 5.5, 5.0, 0.01, 100);
    return 0;
}