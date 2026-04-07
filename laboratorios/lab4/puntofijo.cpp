#include <iostream>
#include <cmath>

double f(double x) {
    return (2 * std::exp(x * x)) - (5 * x); // ECUACION ORIGINAL f(x)
}

double g(double x) {
    return 0.4 * std::exp(x * x); // ECUACION IGUALADA A CERO DE LA FORMA x=g(x)
}

void punto_fijo(double x0, double error) {
    double e = 100;
    double xi = 0;
    int k = 0;
    int n = 0;

    while (n < 50) {
        if (e > error) {
            double xn = g(xi);
            e = std::abs((xn - xi) / xn);
            xi = xn;
            k++;
            double porcentaje = e * 100;
            std::cout << "iteracion #" << k << " con valor de raiz = " << xn << " con un error de: " << e << std::endl;
        }
        n++;
    }
}

int main() {
punto_fijo(0, 0.01); // VARIABLES: Valor inicial, error estimado
return 0;
}