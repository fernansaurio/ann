#include <stdio.h>
#include <math.h>

// Definición de la función (Cambia esta expresión según lo necesites)
// Ejemplo: f(x) = x^3 - x - 2
double f(double x) {
    return pow(x, 3) - x - 2;
}

int main() {
    double x0, x1, x_sig, tol, error;
    int max_iter, i;

    printf("--- Metodo de la Secante en C ---\n");
    
    // Entrada de datos
    printf("Ingrese x0 (primer punto inicial): ");
    scanf("%lf", &x0);
    printf("Ingrese x1 (segundo punto inicial): ");
    scanf("%lf", &x1);
    printf("Ingrese la tolerancia (ej. 0.0001): ");
    scanf("%lf", &tol);
    printf("Maximo de iteraciones: ");
    scanf("%d", &max_iter);

    printf("\n%-5s | %-12s | %-12s | %-12s\n", "Iter", "xi", "f(xi)", "Error");
    printf("------------------------------------------------------------\n");

    for (i = 1; i <= max_iter; i++) {
        double fx0 = f(x0);
        double fx1 = f(x1);

        // Verificación de división por cero
        if (fabs(fx1 - fx0) < 1e-15) {
            printf("Error: Pendiente nula (division por cero).\n");
            return 1;
        }

        // Fórmula de la Secante
        x_sig = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0);
        error = fabs(x_sig - x1);

        // Imprimir resultados de la iteración
        printf("%-5d | %-12.6f | %-12.6f | %-12.6e\n", i, x_sig, f(x_sig), error);

        // Criterio de parada
        if (error < tol) {
            printf("\nRaiz encontrada: %.6f con error %.6e\n", x_sig, error);
            return 0;
        }

        // Actualización de variables
        x0 = x1;
        x1 = x_sig;
    }

    printf("\nEl metodo no convergio tras %d iteraciones.\n", max_iter);
    return 0;
}