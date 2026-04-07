from math import *
import sympy as sp
from sympy import Symbol
from sympy.plotting import plot
from numpy import *
import numpy as np
import pylab as plt
from matplotlib import *

def NewtonRaphson (x0,error,n):
    x=sp.Symbol('x')
    y=(1/(e**x)-x) #Ecuacion
    dy=sp.diff(y)
    y=sp.lambdify(x,y)
    dy=sp.lambdify(x,dy)
    for k in range (n):
        x1=x0-y(x0)/dy(x0); #paso 2
        ea=(x1-x0)/x1; #paso 3
        if (abs((x1-x0)/x1)<error):
            print("iteracion #",k+1,"con un valor de raiz de: ")
            print(x1," con un error de ",ea)
            return
        x0=x1
    print ("iteracion #", k+1, "con un valor de raiz de: ")
    print (x1, " con un error de ",ea)
NewtonRaphson(0,0.01,50); # (valo inicial X0, valor del error,
# rango (esto no es necesario
# modificar))