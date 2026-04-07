// Newton - Raphson 

#include <iostream>

extern "C" {
    // Valor absoluto manual
    double my_abs(double n) {
        return (n < 0) ? -n : n;
    }

    double my_sqrt(double s) {
    if (s <= 0) return 0;
    double x = s;
    double y = 1;
    double e = 0.000001; // Precisión interna
    while (my_abs(x - y) > e) {
        x = (x + y) / 2;
        y = s / x;
    }
    return x;
    }
    
    double my_sin(double x) {
        double term = x;
        double sum = x;
        for (int i = 1; i < 20; i++) {
            // Genera el siguiente término: (-1)^n * x^(2n+1) / (2n+1)!
            term = -term * x * x / ((2 * i) * (2 * i + 1));
            sum += term;
        }
        return sum;
    }
    double my_cos(double x) {
        double term = 1.0, sum = 1.0;
        for (int i = 1; i < 20; i++) {
            term = -term * x * x / ((2 * i - 1) * (2 * i));
            sum += term;
        }
        return sum;
    }
      
    // Función del Ejercicio 3: f(x) = 2 sen(sqrt(x))- x
    double f(double x) {
        return 2.0 * my_sin(my_sqrt(x)) - x;
    }

    // Derivada: f'(x) = -e^-x - 1
    double df(double x) {
        return (my_cos(my_sqrt(x))/my_sqrt(x)) - 1.0;
    }

    // Algoritmo de Newton-Raphson
    double calcular_newton(double x0, double error_obj) {
        double xi = x0;
        double ea = 100.0;
        double xi_ant;
        
        while (ea > error_obj) {
            xi_ant = xi;
            // Fórmula: x_{i+1} = x_i - f(x_i)/f'(x_i)
            xi = xi_ant - (f(xi_ant) / df(xi_ant));
            
            if (xi != 0) {
                ea = my_abs((xi - xi_ant) / xi) * 100.0;
            }
        }
        return xi;
    }
}