//3. Remache: valor verdadero de 2cm y valor verdadero de 1.87cm

#include <iostream>
using namespace std;
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
    double v_real = 2.0;
    double v_aproximado = 1.87;

    cout << "Valor verdadero: " << v_real << " cm" << endl;
    cout << "Valor aproximado: " << v_aproximado << " cm" << endl;

    double errorV = error_verdadero(v_real, v_aproximado);
    double errorR = error_relativo(v_real, v_aproximado);

    cout << "Error verdadero: " << errorV << " cm" << endl;
    cout << "Error relativo: " << errorR << " %" << endl;

    return 0;
}