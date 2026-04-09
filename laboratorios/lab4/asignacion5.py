"""
UNIVERSIDAD DE EL SALVADOR 
FACULTAD DE INGENIERIA Y ARQUITECTURA

Analisis Numérico
Laboratorio 4 - Asignacion 5

Alumnos:
Oscar Manuel Velasquez Villanueva vv24002
Diego Josué Mendoza Prudencio MP24048
Marcelo Xavier Molina Gómez MG24048
Fernando José Padilla Cruz PC24039
Mauricio Antonio Muñoz Contreras MC24021 
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x): return 2*x**3 - 11.7*x**2 + 17.7*x - 5
def df(x): return 6*x**2 - 23.4*x + 17.7
def g(x): return ((11.7*x**2 - 17.7*x + 5) / 2.0)**(1/3) # Para Punto Fijo

# a) Método Gráfico
x_vals = np.linspace(0, 4, 100)
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='red')
plt.title("5a) Método Gráfico")
plt.grid(True)
plt.show()

print("--- b) Punto Fijo (3 iteraciones, x0=3) ---")
x0 = 3.0
for i in range(1, 4):
    x1 = g(x0)
    print(f"Iter {i}: x = {x1:.6f}")
    x0 = x1

print("\n--- c) Newton-Raphson (3 iteraciones, x0=3) ---")
x0 = 3.0
for i in range(1, 4):
    x1 = x0 - f(x0)/df(x0)
    print(f"Iter {i}: x = {x1:.6f}")
    x0 = x1

print("\n--- d) Comprobación de Resultados ---")
print(f"Evaluando la raíz hallada por NR f({x0:.6f}) = {f(x0):.8f}")