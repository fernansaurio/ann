/*
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 2 - Asignacion 5

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
*/

/*
Desarrolle la serie de Maclaurin en C y resuelva para 𝑒
0.5
con 6 términos de la serie.
Nota: para comprobar el resultado, este debe ser igual al de la iteración 6 del ejemplo 2
de la guía de laboratorio.
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
    float x = 0.5;
    double resultado = e_x(x);
    cout << "El resultado de e^" << x << " es: " << resultado << endl;

    double valor_real = 1.64872; // Valor real de e^0.5
    double errorV = error_verdadero(valor_real, resultado);
    double errorR = error_relativo(valor_real, resultado);
    cout << "Error verdadero: " << errorV << endl;
    cout << "Error relativo porcentual: " << errorR << "%" << endl;
    return 0;
}
