#include <stdio.h>
#include <math.h>

double g(double x) {
    return 2.0 * sin(sqrt(x));
}

int main() {
    double x0 = 0.5, x1, error_target = 0.00001; // 0.001%
    double ea = 100.0;
    int iter = 0;

    printf("Iter | Raiz         | Error\n");
    while (ea > error_target && iter < 100) {
        x1 = g(x0);
        ea = fabs((x1 - x0) / x1) * 100;
        x0 = x1;
        iter++;
        printf("%d    | %f     | %f%%\n", iter, x1, ea);
    }
    return 0;
}