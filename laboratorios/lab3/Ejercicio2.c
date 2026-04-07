// Ejercicio 2: Método de Punto Fijo 

#include <stdio.h>

// --- FUNCIONES MATEMÁTICAS MANUALES ---

// Valor absoluto manual
double my_abs(double n) {
    return (n < 0) ? -n : n;
}

// Raíz cuadrada manual (Método de Newton/Babilónico)
double my_sqrt(double s) {
    if (s <= 0) return 0;
    double x = s;
    double y = 1;
    double e = 0.000001; // Precisión interna
    while (my_abs(x - y) > e) {
        x = (x + y) / 2;
        y = s / x;
    }
    return x;
}

// Seno manual (Serie de Maclaurin)
double my_sin(double x) {
    double term = x;
    double sum = x;
    for (int i = 1; i < 20; i++) {
        // Genera el siguiente término: (-1)^n * x^(2n+1) / (2n+1)!
        term = -term * x * x / ((2 * i) * (2 * i + 1));
        sum += term;
    }
    return sum;
}

// --- MÉTODO DE PUNTO FIJO ---

double g(double x) {
    // g(x) = 2 * sen(sqrt(x))
    return 2.0 * my_sin(my_sqrt(x));
}

void punto_fijo(double x0, double error_objetivo, int max_iter) {
    double xi = x0;
    double xn;
    double ea = 100.0;
    int k = 0;

    printf("\nIter |      xi      |  Err. Prcnt %%\n");
    printf("------------------------------------\n");

    while (ea > error_objetivo && k < max_iter) {
        xn = g(xi);
        if (xn != 0) {
            ea = (my_abs(xn - xi) / xn) * 100.0;
        }
        xi = xn;
        k++;
        printf("%-4d | %-12.6f | %-12.6f%%\n", k, xi, ea);
    }
    printf("------------------------------------\n");
    printf("Resultado -> Raiz: %.6f | Iteraciones: %d\n", xi, k);
}

int main() {
    // Parámetros: x0=0.5, Error=0.001%, Max_Iter=50
    punto_fijo(0.5, 0.001, 50);
    return 0;
}