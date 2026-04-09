"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 4 - Asignacion 3

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): return x**2 - 4
def df(x): return 2*x

x0 = 5.0
x_vals = [x0]

# Iteraciones de Newton-Raphson
for i in range(4):
    x_new = x0 - f(x0)/df(x0)
    x_vals.append(x_new)
    x0 = x_new

# Preparar la gráfica
x = np.linspace(0, 6, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="f(x) = x^2 - 4", color="blue")
plt.axhline(0, color="black", linewidth=1)

# Graficar iteraciones y tangentes
for i in range(len(x_vals)-1):
    xi = x_vals[i]
    plt.plot(xi, f(xi), 'ro') # Punto en la curva
    plt.plot([xi, xi], [0, f(xi)], 'r--') # Línea vertical al eje X
    
    # Línea tangente
    x_tangent = np.linspace(x_vals[i+1]-1, xi+1, 10)
    y_tangent = df(xi) * (x_tangent - xi) + f(xi)
    plt.plot(x_tangent, y_tangent, 'g--', alpha=0.5)

plt.title("Método de Newton-Raphson Visualizado")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()