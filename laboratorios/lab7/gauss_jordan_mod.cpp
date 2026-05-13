#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;

const int MAX_N = 10;

/* Metodo de Gauss-Jordan generalizado.
   n = numero de variables (1 hasta MAX_N)
   matrix: vector aumentado [n x (n+1)] */
void gaussJordan(vector<vector<double>>& matrix, int n) {
    for (int i = 0; i < n; i++) {
        /* Pivoteo parcial con valor absoluto */
        int max_row = i;
        for (int k = i + 1; k < n; k++)
            if (fabs(matrix[k][i]) > fabs(matrix[max_row][i]))
                max_row = k;

        /* Intercambio de filas */
        swap(matrix[i], matrix[max_row]);

        /* Verificar singularidad */
        if (fabs(matrix[i][i]) < 1e-12) {
            cout << "Sistema singular o sin solucion unica." << endl;
            return;
        }

        /* Hacer elemento diagonal igual a 1 */
        double divisor = matrix[i][i];
        for (int k = i; k <= n; k++)
            matrix[i][k] /= divisor;

        /* Hacer ceros en TODA la columna (arriba y abajo) */
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = matrix[k][i];
                for (int j = i; j <= n; j++)
                    matrix[k][j] -= factor * matrix[i][j];
            }
        }
    }
}

/* Mostrar la matriz aumentada con formato */
void display(const vector<vector<double>>& matrix, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++)
            cout << fixed << setprecision(4) << setw(9) << matrix[i][j] << " ";
        cout << "\n";
    }
}

int main() {
    /* -------------------------------------------------------
       Sistema 1 (imagen):
         2x1 +  x2 -  x3 =  1
         5x1 + 2x2 + 2x3 = -4
         3x1 +  x2 +  x3 =  5
    ------------------------------------------------------- */
    int n1 = 3;
    vector<vector<double>> m1 = {
        {2,  1, -1,  1},
        {5,  2,  2, -4},
        {3,  1,  1,  5}
    };

    cout << "=== Sistema 1 ===" << endl;
    cout << "Matriz original:" << endl;
    display(m1, n1);
    gaussJordan(m1, n1);
    cout << "Solucion:" << endl;
    for (int i = 0; i < n1; i++)
        cout << "x" << i + 1 << " = " << fixed << setprecision(4) << m1[i][n1] << "\n";

    /* -------------------------------------------------------
       Sistema 2 (imagen):
          x1 +  x2 -  x3 = -3
         6x1 + 2x2 + 2x3 =  2
        -3x1 + 4x2 +  x3 =  1
    ------------------------------------------------------- */
    int n2 = 3;
    vector<vector<double>> m2 = {
        { 1,  1, -1, -3},
        { 6,  2,  2,  2},
        {-3,  4,  1,  1}
    };

    cout << "\n=== Sistema 2 ===" << endl;
    cout << "Matriz original:" << endl;
    display(m2, n2);
    gaussJordan(m2, n2);
    cout << "Solucion:" << endl;
    for (int i = 0; i < n2; i++)
        cout << "x" << i + 1 << " = " << fixed << setprecision(4) << m2[i][n2] << "\n";

    return 0;
}
