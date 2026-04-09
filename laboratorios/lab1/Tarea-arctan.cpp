/*
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 1 - Asignacion 1

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

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