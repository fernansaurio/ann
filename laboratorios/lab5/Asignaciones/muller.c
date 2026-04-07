#include <stdio.h>
#include <math.h>

// Función de prueba: f(x) = x^3 - 13x - 12
double f(double x) {
    return pow(x, 3) - 13 * x - 12;
}

void muller_seguro(double x0, double x1, double x2, double tol, int max_iter) {
    double h1, h2, d1, d2, a, b, c, radical, den, dx, x3;
    int i;

    printf("\n%-5s | %-12s | %-12s\n", "Iter", "x3", "f(x3)");
    printf("---------------------------------------\n");

    for (i = 1; i <= max_iter; i++) {
        h1 = x1 - x0;
        h2 = x2 - x1;
        d1 = (f(x1) - f(x0)) / h1;
        d2 = (f(x2) - f(x1)) / h2;

        a = (d2 - d1) / (h2 + h1);
        b = a * h2 + d2;
        c = f(x2);

        double discriminante = b * b - 4 * a * c;

        // --- RESTRICCIÓN PARA VALORES NO REALES O INDETERMINADOS ---
        if (discriminante < 0) {
            printf("\n[!] Error: El discriminante es negativo (%.4f).\n", discriminante);
            printf("El metodo requiere numeros complejos para continuar.\n");
            return;
        }

        radical = sqrt(discriminante);

        if (fabs(b + radical) > fabs(b - radical)) {
            den = b + radical;
        } else {
            den = b - radical;
        }

        // Validación de división por cero antes de calcular dx
        if (fabs(den) < 1e-18) {
            printf("\n[!] Error: Denominador nulo. No se puede calcular x3.\n");
            return;
        }

        dx = (-2 * c) / den;
        x3 = x2 + dx;

        // --- CHEQUEO DE NAN ---
        if (isnan(x3) || isnan(f(x3))) {
            printf("\n[!] Alerta: Se ha detectado un valor NaN en la iteracion %d.\n", i);
            printf("Prueba con diferentes valores iniciales.\n");
            return;
        }

        printf("%-5d | %-12.6f | %-12.6e\n", i, x3, f(x3));

        if (fabs(dx) < tol) {
            printf("\nRaiz encontrada en: %.6f\n", x3);
            return;
        }

        x0 = x1;
        x1 = x2;
        x2 = x3;
    }

    printf("\nEl metodo no convergio.\n");
}

int main() {
// Puntos sugeridos para x^3 - 13x - 12: 4.5, 5, 5.5 (Raiz en 4)
    muller_seguro(4.5, 5.0, 5.5, 1e-6, 50);
    return 0;
}