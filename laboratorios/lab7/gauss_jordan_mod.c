#include <stdio.h>
#include <math.h>
#define MAX_N 10

void gaussJordan(double matrix[MAX_N][MAX_N+1], int n) {
    for (int i = 0; i < n; i++) {
        /* Pivoteo parcial */
        int max_row = i;
        for (int k = i + 1; k < n; k++) {
            if (fabs(matrix[k][i]) > fabs(matrix[max_row][i]))
                max_row = k;
        }
        /* Intercambio de filas */
        for (int k = i; k <= n; k++) {
            double temp = matrix[i][k];
            matrix[i][k] = matrix[max_row][k];
            matrix[max_row][k] = temp;
        }
        /* Verificar singularidad */
        if (fabs(matrix[i][i]) < 1e-12) {
            printf("Sistema singular o sin solucion unica.\n");
            return;
        }
        /* Hacer diagonal == 1 */
        double divisor = matrix[i][i];
        for (int k = i; k <= n; k++)
            matrix[i][k] /= divisor;
        /* Hacer ceros en toda la columna */
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = matrix[k][i];
                for (int j = i; j <= n; j++)
                    matrix[k][j] -= factor * matrix[i][j];
            }
        }
    }
}

void display(double matrix[MAX_N][MAX_N+1], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++)
            printf("%8.4f ", matrix[i][j]);
        printf("\n");
    }
}

int main() {
    /* --- Sistema 1 (imagen) --- */
    int n1 = 3;
    double m1[MAX_N][MAX_N+1] = {
        {2, 1, -1,  1},
        {5, 2,  2, -4},
        {3, 1,  1,  5}
    };
    printf("=== Sistema 1 ===\n");
    gaussJordan(m1, n1);
    for (int i = 0; i < n1; i++)
        printf("x%d = %.4f\n", i+1, m1[i][n1]);

    /* --- Sistema 2 (imagen) --- */
    int n2 = 3;
    double m2[MAX_N][MAX_N+1] = {
        { 1,  1, -1, -3},
        { 6,  2,  2,  2},
        {-3,  4,  1,  1}
    };
    printf("\n=== Sistema 2 ===\n");
    gaussJordan(m2, n2);
    for (int i = 0; i < n2; i++)
        printf("x%d = %.4f\n", i+1, m2[i][n2]);

    return 0;
}