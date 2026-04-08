#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double f(double x) {
    return -0.4 * x * x + 2.3 * x + 2.2;
}

int main() {
    double xa = 6.0, xb = 7.0, xc, error = 100.0;
    double tol = 0.001; 
    int iter = 1, max_iter = 100;

    cout << "--- Metodo de la Secante (C++) ---" << endl;
    cout << setw(5) << "Iter" << setw(15) << "xa" << setw(15) << "xb" 
         << setw(15) << "xc" << setw(15) << "Error %" << endl;
    
    while (error > tol && iter < max_iter) {
        double fa = f(xa);
        double fb = f(xb);
        
        xc = xa - fa * (xb - xa) / (fb - fa);
        error = abs((xc - xa) / xc) * 100.0;
        
        cout << setw(5) << iter << setw(15) << fixed << setprecision(6) << xa 
             << setw(15) << xb << setw(15) << xc << setw(15) << error << endl;
        
        xa = xb;
        xb = xc;
        iter++;
    }
    cout << "\nRaiz aproximada: " << xc << endl;
    return 0;
}