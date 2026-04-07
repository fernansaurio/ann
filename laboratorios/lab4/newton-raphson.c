#include <stdio.h>
#include <math.h>

// f(x) = e^(-x) - x
double f(double x) {
    return (1.0 / exp(x)) - x;
}

// f'(x) = -e^(-x) - 1
double df(double x) {
    return (-1.0 / exp(x)) - 1.0;
}

void NewtonRaphson(double x0, double error, int max_iter) {
    double xi = x0;
    
    for (int k = 0; k < max_iter; ++k) {
        double fxi = f(xi);
        double dfxi = df(xi);

        // Verificamos que la derivada no sea cero para evitar división por cero
        if (dfxi == 0) {
            printf("Derivada nula. El método falla.\n");
            return;
        }

        double xn = xi - fxi / dfxi;            // Fórmula de Newton-Raphson
        double ea = fabs((xn - xi) / xn);       // Error relativo

        printf("Iteracion #%d: raiz aproximada = %lf, error = %lf\n", k + 1, xn, ea);

        // Si alcanzamos la precisión deseada, terminamos
        if (ea < error) {
            printf("\nConvergencia alcanzada en %d iteraciones!\n", k + 1);
            printf("Raiz final: %lf con error de %lf\n", xn, ea);
            return;
        }

        xi = xn; // Actualizamos para la siguiente iteración
    }

    printf("\nSe alcanzó el número máximo de iteraciones (%d).\n", max_iter);
    printf("Última aproximación = %lf\n", xi);
}

int main() {
    double x0 = 0.5;      // Valor inicial (ajustado de 0 a 0.5 para mejor convergencia)
    double error = 0.01;  // Tolerancia
    int max_iter = 10;    // Aumentamos a 10 para asegurar que encuentre la raíz

    printf("--- Metodo de Newton-Raphson ---\n");
    NewtonRaphson(x0, error, max_iter);

    return 0;
}