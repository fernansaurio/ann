/*UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 5 - Asignacion 7

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

#include <stdio.h>
#include <math.h>

double f(double R) {
    double exp_term = exp(-0.005 * R);
    double cos_term = cos(0.05 * sqrt(2000.0 - 0.01 * R * R));
    return exp_term * cos_term - 0.01;
}

int main() {
    double a = 320.0, b = 330.0, c_bisect, c_falsa, c_prev = 0.0;
    double tol = 0.0001;
    
    printf("--- Ejercicio RLC: Biseccion ---\n");
    for(int i=1; i<=20; i++) {
        c_bisect = (a + b) / 2.0;
        double error = fabs((c_bisect - c_prev)/c_bisect) * 100.0;
        if(i==20) {
            printf("Iter 20 Biseccion: R = %.4f, Error = %.4f%%\n", c_bisect, error);
        }
        if(f(a)*f(c_bisect) < 0) b = c_bisect;
        else a = c_bisect;
        c_prev = c_bisect;
    }

    // Reiniciar para Falsa Posicion
    a = 320.0; b = 330.0; c_prev = 0.0;
    printf("\n--- Ejercicio RLC: Falsa Posicion ---\n");
    for(int i=1; i<=20; i++) {
        c_falsa = b - (f(b)*(a - b)) / (f(a) - f(b));
        double error = fabs((c_falsa - c_prev)/c_falsa) * 100.0;
        if(error < tol) {
            printf("Raiz Falsa Posicion: R = %.4f en %d iteraciones\n", c_falsa, i);
            break;
        }
        if(f(a)*f(c_falsa) < 0) b = c_falsa;
        else a = c_falsa;
        c_prev = c_falsa;
    }
    return 0;
}