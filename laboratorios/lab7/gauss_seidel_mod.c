#include <stdio.h>
#include <math.h>

#define MAX_N    10
#define MAX_ITER 100
#define ES       0.0005   /* criterio de parada en % */

/* Metodo de Gauss-Seidel con deteccion de convergencia/divergencia.
   A    : matriz aumentada [n x (n+1)]  [coef | b]
   x    : vector solución inicial (se actualiza in-place)
   n    : numero de variables
   Retorna 1 = convergio, 0 = divergio */
int gaussSeidel(double A[MAX_N][MAX_N + 1], double x[],
                int n, int max_iter, double es) {
    double x_prev[MAX_N];

    /* Encabezado de tabla */
    printf("%-5s", "Iter");
    for (int i = 0; i < n; i++)
        printf("     x%d     ", i + 1);
    printf("  ea_max(%%)\n");

    for (int iter = 1; iter <= max_iter; iter++) {
        /* Guardar valores de iteracion anterior */
        for (int i = 0; i < n; i++) x_prev[i] = x[i];

        /* Calcular nuevos valores */
        for (int i = 0; i < n; i++) {
            double sum = A[i][n];
            for (int j = 0; j < n; j++)
                if (j != i) sum -= A[i][j] * x[j];
            x[i] = sum / A[i][i];
        }

        /* Calcular error relativo aproximado maximo
           ea = |(x_nuevo - x_anterior) / x_nuevo| * 100 */
        double ea_max = 0.0;
        int    diverge = 0;
        for (int i = 0; i < n; i++) {
            double ea = (x[i] != 0.0)
                        ? fabs((x[i] - x_prev[i]) / x[i]) * 100.0
                        : fabs(x[i] - x_prev[i]);
            if (ea > ea_max) ea_max = ea;
            if (fabs(x[i]) > 1e10) diverge = 1;
        }

        /* Imprimir fila de la tabla */
        printf("%-5d", iter);
        for (int i = 0; i < n; i++)
            printf("  %10.5f", x[i]);
        printf("  %10.5f\n", ea_max);

        if (diverge) {
            printf("\n*** DIVERGENCIA detectada en iteracion %d ***\n", iter);
            return 0;
        }
        if (ea_max < es) {
            printf("\nConvergencia en iteracion %d  (ea=%.6f%% < es=%.4f%%)\n",
                   iter, ea_max, es);
            return 1;
        }
    }

    printf("\nNo convergio en %d iteraciones -> DIVERGENCIA.\n", max_iter);
    return 0;
}

int main() {
    int n = 3;

    /* -------------------------------------------------------
       Sistema 1 (imagen):
         2x1 +  x2 -  x3 =  1
         5x1 + 2x2 + 2x3 = -4
         3x1 +  x2 +  x3 =  5
       (NO es diagonalmente dominante -> diverge)
    ------------------------------------------------------- */
    double A1[MAX_N][MAX_N + 1] = {
        {2,  1, -1,  1},
        {5,  2,  2, -4},
        {3,  1,  1,  5}
    };
    double x1[MAX_N] = {0};
    printf("=== Sistema 1 imagen — Gauss-Seidel ===\n");
    int ok1 = gaussSeidel(A1, x1, n, MAX_ITER, ES);
    printf("Resultado: %s\n\n", ok1 ? "CONVERGENCIA" : "DIVERGENCIA");

    /* -------------------------------------------------------
       Sistema 2 (imagen):
          x1 +  x2 -  x3 = -3
         6x1 + 2x2 + 2x3 =  2
        -3x1 + 4x2 +  x3 =  1
       (NO es diagonalmente dominante -> diverge)
    ------------------------------------------------------- */
    double A2[MAX_N][MAX_N + 1] = {
        { 1,  1, -1, -3},
        { 6,  2,  2,  2},
        {-3,  4,  1,  1}
    };
    double x2[MAX_N] = {0};
    printf("=== Sistema 2 imagen — Gauss-Seidel ===\n");
    int ok2 = gaussSeidel(A2, x2, n, MAX_ITER, ES);
    printf("Resultado: %s\n\n", ok2 ? "CONVERGENCIA" : "DIVERGENCIA");

    /* -------------------------------------------------------
       Sistema original del enunciado (referencia):
         4x1 -   x2 + 0.2x3 = 8
          x1 +  5x2 + 0.3x3 = 7
        0.1x1 + 0.2x2 + 3x3 = 5
       (Diagonalmente dominante -> converge)
    ------------------------------------------------------- */
    double A3[MAX_N][MAX_N + 1] = {
        {4,   -1,  0.2, 8},
        {1,    5,  0.3, 7},
        {0.1, 0.2, 3.0, 5}
    };
    double x3[MAX_N] = {0};
    printf("=== Sistema original — Gauss-Seidel ===\n");
    int ok3 = gaussSeidel(A3, x3, n, MAX_ITER, ES);
    printf("Resultado: %s\n", ok3 ? "CONVERGENCIA" : "DIVERGENCIA");
    if (ok3)
        for (int i = 0; i < n; i++)
            printf("x%d = %.5f\n", i + 1, x3[i]);

    return 0;
}
