#include <iostream>
#include <cmath>
#include <iomanip>

double f(double x) { return 2*sin(sqrt(x)) - x; }
double df(double x) { return cos(sqrt(x))/sqrt(x) - 1; }

int main() {
    double xi = 0.5, xr, error = 0.001;
    std::cout << std::fixed << std::setprecision(6);
    for(int i=0; i<10; ++i) {
        xr = xi - f(xi)/df(xi);
        std::cout << "Iter " << i+1 << ": " << xr << std::endl;
        xi = xr;
    }
    return 0;
}