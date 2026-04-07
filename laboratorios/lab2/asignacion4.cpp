/*
4. Dada la serie de Maclaurin, estime el valor de 𝑒
1.6 de modo que sea exacto en al menos
3 cifras significativas. Considere el valor verdadero de 𝑒
1.6 = 4.953032
*/

#include <iostream>

using namespace std;

double e_x(float x){
    double sum = 1 + x;
    int fac = 2;
    double x_acu = x*x; 

        for (int i = 2; i<25; i++){
            sum += x_acu/fac;
                x_acu = x_acu * x;
                fac = fac * (i+1);
        }

    return sum;
}

double error_verdadero(double v_real, double v_aproximado){
    double a = (v_real - v_aproximado);
    if (a < 0){
        a = a * -1;
        return a;
    }
    else{
        return a;
    }
}

double error_relativo(double v_real, double v_aproximado){
    double a = (((v_real - v_aproximado) / v_real)*100);
    if (a<0){
        a = a * -1;
        return a;
    }
    else{
        return a;
    }
}

int main() {
    float x = 1.6;
    double valor_aproximado = e_x(x);
    double valor_verdadero = 4.953032;

    cout << "Valor aproximado de e^1.6: " << valor_aproximado << endl;
    cout << "Valor verdadero de e^1.6: " << valor_verdadero << endl;
    cout << "Error verdadero: " << error_verdadero(valor_verdadero, valor_aproximado) << endl;
    cout << "Error relativo (%): " << error_relativo(valor_verdadero, valor_aproximado) << "%" << endl;

    return 0;
}