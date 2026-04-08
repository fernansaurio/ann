// 2. Puente: valor verdadero de 20m y valor medido de 19.6m


#include <iostream>

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

int main(){
    double val_real = 20; // valor Verdadero
    double val_aprox = 19.6; // valor aproximado

    // calculo del error verdadero
    double Ev = error_verdadero(val_real, val_aprox);

    // calculo del error relativo porcentual
    double Er = error_relativo(val_real, val_aprox);

    // muestra el error verdadero
    std::cout << "Error verdadero: " << Ev << "\n";

    // muestra el error relativo porcentual
    std::cout << "Error relativo porcentual: " << Er << "%\n";
    
    return 0;
}
