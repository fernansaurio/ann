#include <iostream>
#include <cmath>
using namespace std;
// Funcion para la cual queremos encontrar la raiz
double f(double x) {
return x * x * x - 13 * x - 12;; // Ejemplo: x^2 - 5
}
// Metodo de Muller
void muller(double x0, double x1, double x2, double tol, int
max_iter) {
double h1 = x1 - x0;
double h2 = x2 - x1;
double d1 = (f(x1) - f(x0)) / h1;
double d2 = (f(x2) - f(x1)) / h2;
double a = (d2 - d1) / (h2 + h1);
double b = a * h2 + d2;
double c = f(x2);
double discriminant = b * b - 4 * a * c;
double x3;
for (int i = 0; i < max_iter; ++i) {
if (discriminant < 0) {
cout << "Error: Discriminant is negative. Cannot continue." << endl;
return;
}
double sqrt_discriminant = sqrt(discriminant);
double den = (b < 0) ? b - sqrt_discriminant : b +
sqrt_discriminant;
x3 = x2 - (2 * c) / den;
double error = fabs((x3 - x2)/x3)*100;
cout << "Iteration " << i + 1 << ": Raiz aproximada = " <<
x3 << ", Error % = " << error << endl;
if (error < tol) {
cout << "Resultado de la Raiz = " << x3 << endl;
return;
}
x0 = x1;
x1 = x2;
x2 = x3;
h1 = x1 - x0;
h2 = x2 - x1;
d1 = (f(x1) - f(x0)) / h1;
d2 = (f(x2) - f(x1)) / h2;
a = (d2 - d1) / (h2 + h1);
b = a * h2 + d2;
c = f(x2);
discriminant = b * b - 4 * a * c;
}
cout << "Maximum iterations reached. No convergence." << endl;
}
int main() {
double x0 = 4.5; // Initial guess 1
double x1 = 5.5; // Initial guess 2
double x2 = 5; // Initial guess 3
double tolerance = 0.01; // Tolerance for convergence
int max_iterations = 100; // Maximum number of iterations
muller(x0, x1, x2, tolerance, max_iterations);
return 0;
}