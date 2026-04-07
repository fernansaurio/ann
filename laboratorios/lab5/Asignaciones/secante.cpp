#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Definimos la función de la cual queremos hallar la raíz
// Nota: En C++, para cambiar la función debes editar esta sección
double f(double x) {
    return pow(x, 2) - 2; // Ejemplo: f(x) = x^2 - 2
}

void metodoSecante(double x0, double x1, double tol, int max_iter) {
    double x_sig;
    double error;
    
    cout << fixed << setprecision(6);
    cout << "Iter. |      x_i     |     f(x_i)   |    Error    " << endl;
    cout << "----------------------------------------------------" << endl;

    for (int i = 1; i <= max_iter; ++i) {
        double fx0 = f(x0);
        double fx1 = f(x1);

        if (abs(fx1 - fx0) < 1e-15) {
            cout << "Error: División por cero." << endl;
            return;
        }

        // Fórmula de la Secante
        x_sig = x1 - fx1 * (x1 - x0) / (fx1 - fx0);
        error = abs(x_sig - x1);

        cout << setw(5) << i << " | " 
             << setw(12) << x_sig << " | " 
             << setw(12) << f(x_sig) << " | " 
             << setw(10) << error << endl;

        if (error < tol) {
            cout << "\nRaiz encontrada en: " << x_sig << endl;
            return;
        }

        // Actualizamos para la siguiente iteración
        x0 = x1;
        x1 = x_sig;
    }

    cout << "\nSe alcanzó el máximo de iteraciones sin converger." << endl;
}

int main() {
    double x0, x1, tolerancia;
    int iteraciones;

    cout << "--- Metodo de la Secante (C++) ---" << endl;
    cout << "Ingrese x0: "; cin >> x0;
    cout << "Ingrese x1: "; cin >> x1;
    cout << "Tolerancia (ej. 0.0001): "; cin >> tolerancia;
    cout << "Max. Iteraciones: "; cin >> iteraciones;

    metodoSecante(x0, x1, tolerancia, iteraciones);

    return 0;
}