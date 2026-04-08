#include <cmath>

// f(x) = x^2 - 4
double f(double x) {
    return x * x - 4.0;
}

// f'(x) = 2x
double df(double x) {
    return 2.0 * x;
}

extern "C" {
    // Función que será exportada a Python.
    // Retorna la raíz encontrada.
    // Además, llena el arreglo 'history' con los valores de x para que Python pueda graficarlos,
    // y actualiza 'iters_used' con la cantidad de iteraciones reales.
    double newton_raphson(double x0, double tol, int max_iter, int* iters_used, double* history) {
        double x1 = x0;
        double error = 100.0;
        int iter = 0;
        
        history[0] = x0; // Guardar el valor inicial
        
        while (error > tol && iter < max_iter) {
            double derivada = df(x0);
            
            // Evitar división por cero
            if (derivada == 0.0) {
                *iters_used = iter;
                return x0; 
            }
            
            x1 = x0 - (f(x0) / derivada);
            error = std::abs((x1 - x0) / x1) * 100.0;
            
            iter++;
            history[iter] = x1;
            x0 = x1;
        }
        
        *iters_used = iter;
        return x1;
    }
}