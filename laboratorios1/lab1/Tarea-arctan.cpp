#include <iostream>
using namespace std;

float exp(float base, float exponente);

float x;
float result = 0;

int main() {
    cout << "Calcular arctan de x \n Ingrese el valor de x (entre -1 y 1): ";
    cin >> x;

    for(int i = 0; i <= 1000; i++) {

        result += (exp(-1, i) / (2 * i + 1)) * (exp(x, (2 * i + 1)));
        cout<<result;
    }

    cout << "Resultado: " << result << endl;
    return 0;
}

float exp(float base, float exponente) {
    float res = 1.0; 

    for(int i = 0; i < exponente; i++) {
        res *= base;
    }
    return res;
}