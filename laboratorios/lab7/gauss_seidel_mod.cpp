#include <iostream>
#include <iomanip>
#include <cmath>
#include <array>
#include <string>
using namespace std;

const int    MAX_N    = 10;
const int    MAX_ITER = 100;
const double ES       = 0.0005;  /* criterio de parada en % */

/* Metodo de Gauss-Seidel con deteccion de convergencia/divergencia.
   A        : matriz aumentada [MAX_N x (MAX_N+1)]  [coef | b]
   x        : vector solucion inicial (se actualiza in-place)
   n        : numero de variables
   Retorna true = convergio, false = divergio */
bool gaussSeidel(const array<array<double, MAX_N + 1>, MAX_N>& A,
                 array<double, MAX_N>& x, int n,
                 int max_iter, double es) {
    array<double, MAX_N> x_prev;

    /* Encabezado de tabla */
    cout << left << setw(5) << "Iter";
    for (int i = 0; i < n; i++)
        cout << setw(12) << ("x" + to_string(i + 1));
    cout << setw(14) << "ea_max(%)" << "\n";

    for (int iter = 1; iter <= max_iter; iter++) {
        /* Guardar valores de iteracion anterior */
        x_prev = x;

        /* Calcular nuevos valores */
        for (int i = 0; i < n; i++) {
            double sum = A[i][n];
            for (int j = 0; j < n; j++)
                if (j != i) sum -= A[i][j] * x[j];
            x[i] = sum / A[i][i];
        }

        /* Calcular error relativo aproximado maximo
           ea = |(x_nuevo - x_anterior) / x_nuevo| * 100 */
        double ea_max  = 0.0;
        bool   diverge = false;
        for (int i = 0; i < n; i++) {
            double ea = (x[i] != 0.0)
                        ? fabs((x[i] - x_prev[i]) / x[i]) * 100.0
                        : fabs(x[i] - x_prev[i]);
            if (ea > ea_max) ea_max = ea;
            if (fabs(x[i]) > 1e10) diverge = true;
        }

        /* Imprimir fila de la tabla */
        cout << left << setw(5) << iter << fixed << setprecision(5);
        for (int i = 0; i < n; i++)
            cout << setw(12) << x[i];
        cout << setw(14) << ea_max << "\n";

        if (diverge) {
            cout << "\n*** DIVERGENCIA detectada en iteracion " << iter << " ***\n";
            return false;
        }
        if (ea_max < es) {
            cout << "\nConvergencia en iteracion " << iter
                 << "  (ea=" << ea_max << "% < es=" << es << "%)\n";
            return true;
        }
    }

    cout << "\nNo convergio en " << max_iter << " iteraciones -> DIVERGENCIA.\n";
    return false;
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
    array<array<double, MAX_N + 1>, MAX_N> A1 = {{
        {2,  1, -1,  1},
        {5,  2,  2, -4},
        {3,  1,  1,  5}
    }};
    array<double, MAX_N> x1 = {0};
    cout << "=== Sistema 1 imagen — Gauss-Seidel ===\n";
    bool ok1 = gaussSeidel(A1, x1, n, MAX_ITER, ES);
    cout << "Resultado: " << (ok1 ? "CONVERGENCIA" : "DIVERGENCIA") << "\n\n";

    /* -------------------------------------------------------
       Sistema 2 (imagen):
          x1 +  x2 -  x3 = -3
         6x1 + 2x2 + 2x3 =  2
        -3x1 + 4x2 +  x3 =  1
       (NO es diagonalmente dominante -> diverge)
    ------------------------------------------------------- */
    array<array<double, MAX_N + 1>, MAX_N> A2 = {{
        { 1,  1, -1, -3},
        { 6,  2,  2,  2},
        {-3,  4,  1,  1}
    }};
    array<double, MAX_N> x2 = {0};
    cout << "=== Sistema 2 imagen — Gauss-Seidel ===\n";
    bool ok2 = gaussSeidel(A2, x2, n, MAX_ITER, ES);
    cout << "Resultado: " << (ok2 ? "CONVERGENCIA" : "DIVERGENCIA") << "\n\n";

    /* -------------------------------------------------------
       Sistema original del enunciado (referencia):
         4x1 -   x2 + 0.2x3 = 8
          x1 +  5x2 + 0.3x3 = 7
        0.1x1 + 0.2x2 + 3x3 = 5
       (Diagonalmente dominante -> converge)
    ------------------------------------------------------- */
    array<array<double, MAX_N + 1>, MAX_N> A3 = {{
        {4,   -1,  0.2, 8},
        {1,    5,  0.3, 7},
        {0.1, 0.2, 3.0, 5}
    }};
    array<double, MAX_N> x3 = {0};
    cout << "=== Sistema original — Gauss-Seidel ===\n";
    bool ok3 = gaussSeidel(A3, x3, n, MAX_ITER, ES);
    cout << "Resultado: " << (ok3 ? "CONVERGENCIA" : "DIVERGENCIA") << "\n";
    if (ok3)
        for (int i = 0; i < n; i++)
            cout << "x" << i + 1 << " = " << x3[i] << "\n";

    return 0;
}
