from math import *
from numpy import *
import numpy as np
import pylab as plt

def f(x):
    return e**(3*x)-4 #colocar funcion y cambiar en linea 26

def biseccion (a,b,error):
    m1=a
    m=b
    k=0
biseccion (0,1,0.01) #cambiar el intervalo y error

if (f(a)*f(b)>0):
    print ("la funcion no cambia de signo")

while (abs(m1-m) > error):
    m1=m
    m=(a+b)/2

if(f(a)*f(m)<0):
    b=m; #intervalo será de "[a,m]"

if(f(b)*f(m)<0):
    b=m; #intervalo será de "[m,b]"

print("'el intervalo es: [",a,",",b,"] error de ", abs(m1- m))
k=k+1
print("iteraciones: ", k," raiz =",m," es una buena aproximación")