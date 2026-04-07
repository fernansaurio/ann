#include <iostream>
#include <iomanip>


int main() {
    double val_real = 10000; // valor Verdadero
    double val_aprox = 9999; // valor aproximado

    // calculo del error verdadero
    double Ev = val_real - val_aprox;

    // calculo del error relativo porcentual
    double Er = ((val_real - val_aprox)/val_real)*100;

    // muestra el error verdadero
    std::cout << "Error verdadero: " << std::fixed <<
    std::setprecision(2) << Ev << "\n";

    // muestra el error relativo porcentual
    std::cout << "Error relativo porcentual: " << std::fixed <<
    std::setprecision(2) << Er << "\n";
    
    return 0;
}