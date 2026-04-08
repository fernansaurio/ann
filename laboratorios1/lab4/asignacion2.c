#include <stdio.h>
#include <math.h>

double g(double x) {
    return 2.0 * sin(sqrt(x));
}

int main() {
    double x0 = 0.5;
    double x1;
    double tolerancia = 0.001;
    double error = 100.0;
    int iteracion = 1;

    printf("Metodo de Punto Fijo en ANSI C\n");
    printf("Iter | x_aprox    | Error (%%)\n");
    printf("-------------------------------\n");

    while (error > tolerancia && iteracion < 100) {
        x1 = g(x0);
        error = fabs((x1 - x0) / x1) * 100.0;
        
        printf(" %2d  | %10.6f | %8.4f%%\n", iteracion, x1, error);
        
        x0 = x1;
        iteracion++;
    }

    printf("\nRaiz encontrada: %10.6f\n", x0);
    return 0;
}