#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// f(x) = x^3 - 5x^2 + 7x - 3
double f(double x) { return pow(x, 3) - 5 * pow(x, 2) + 7 * x - 3; }
// f'(x)
double df(double x) { return 3 * pow(x, 2) - 10 * x + 7; }
// f''(x)
double ddf(double x) { return 6 * x - 10; }

void newton_raphson_modificado(double x0, double tol, int max_iter) {
    double x1, error = 100.0;
    int iter = 1;

    cout << "--- Raices Multiples: N-R Modificado (C++) ---" << endl;
    cout << setw(5) << "Iter" << setw(15) << "xi" << setw(15) << "Error %" << endl;

    while (error > tol && iter <= max_iter) {
        double fx = f(x0);
        double dfx = df(x0);
        double ddfx = ddf(x0);

        // Fórmula NR Modificado: xi+1 = xi - (f(xi)*f'(xi)) / ((f'(xi))^2 - f(xi)*f''(xi))
        double numerador = fx * dfx;
        double denominador = pow(dfx, 2) - (fx * ddfx);
        
        if (denominador == 0) {
            cout << "Error: Division por cero." << endl;
            break;
        }

        x1 = x0 - (numerador / denominador);
        error = abs((x1 - x0) / x1) * 100.0;

        cout << setw(5) << iter << setw(15) << fixed << setprecision(8) << x1 
             << setw(15) << error << endl;

        if (error <= tol) break;
        
        x0 = x1;
        iter++;
    }
    cout << "\nRaiz encontrada: " << x1 << endl;
}

int main() {
    newton_raphson_modificado(0.0, 0.1, 100);
    return 0;
}