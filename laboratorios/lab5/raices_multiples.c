#include <stdio.h>
#include <math.h>

double funcion_ejemplo(double x) {
    return pow(x, 3) - 5 * pow(x, 2) + 7 * x - 3;
}
double derivada_primera_ejemplo(double x) {
    return 3 * pow(x, 2) - 10 * x + 7;
}
double derivada_segunda_ejemplo(double x) {
    return 6 * x - 10;
}

double newton_raphson_modificado(double (*funcion)(double),
double (*derivada_primera)(double), double
(*derivada_segunda)(double), double x_inicial, double tolerancia, int max_iteraciones) {
    double xi = x_inicial;
    double f_xi, f_prime_xi, f_double_prime_xi, xnuevo, error;
        for (int i = 0; i < max_iteraciones; i++) {
            f_xi = funcion(xi);
            f_prime_xi = derivada_primera(xi);
            f_double_prime_xi = derivada_segunda(xi);
            xnuevo = xi - (f_xi * f_prime_xi) / (pow(f_prime_xi, 2) - f_xi * f_double_prime_xi);
            error = fabs((xnuevo - xi) / xnuevo) * 100;
            if (error < tolerancia) {
                break;
            }
            xi = xnuevo;
    }
    printf("\nRaiz: %lf\nerror: %lf", xi, error);
    return error;
}
int main() {
    double tolerancia = 0.1;
    int max_iteraciones = 1000;
    double raiz = newton_raphson_modificado(funcion_ejemplo,
    derivada_primera_ejemplo, derivada_segunda_ejemplo, 0,
    tolerancia, max_iteraciones);
    printf("\nTabla de iteraciones:\n");
    printf("[xi, error]\n");
    // Aqui puedes imprimir la tabla de iteraciones si lo deseas
    return 0;
}